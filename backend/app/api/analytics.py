from collections import defaultdict
from datetime import datetime
from fastapi import APIRouter
from app.core.supabase_client import get_supabase
from app.api.deps import CurrentUser

router = APIRouter(prefix="/analytics", tags=["analytics"])

LEAD_STAGES = ["New", "Qualified", "Proposal", "Won", "Lost"]


@router.get("/dashboard")
async def get_dashboard(current_user: CurrentUser):
    """
    Dashboard stats for SME CRM.
    trend[] uses keys the React charts expect:
      - month (YYYY-MM)
      - leads (new leads that month)  → EngagementChart dataKey="leads"
      - won   (won value that month)  → BalanceChart dataKey="won"
    """
    supabase = get_supabase()
    uid = current_user.id

    leads_res = (
        supabase.table("leads")
        .select("id, status, value, created_at, updated_at, name, company")
        .eq("owner_id", uid)
        .execute()
    )
    contacts_count_res = (
        supabase.table("contacts")
        .select("id", count="exact")
        .eq("owner_id", uid)
        .limit(1)
        .execute()
    )
    tasks_res = (
        supabase.table("tasks")
        .select("id, status")
        .eq("owner_id", uid)
        .execute()
    )

    leads = leads_res.data or []
    tasks = tasks_res.data or []
    total_contacts = (
        contacts_count_res.count
        if contacts_count_res.count is not None
        else len(contacts_count_res.data or [])
    )

    won_value = sum(float(l.get("value") or 0) for l in leads if l.get("status") == "Won")
    total_value = sum(float(l.get("value") or 0) for l in leads)
    by_stage = {s: {"count": 0, "value": 0.0} for s in LEAD_STAGES}
    for l in leads:
        st = l.get("status") or "New"
        if st in by_stage:
            by_stage[st]["count"] += 1
            by_stage[st]["value"] += float(l.get("value") or 0)

    won_count = by_stage["Won"]["count"]
    total_leads = len(leads)
    conversion_rate = round((won_count / total_leads * 100) if total_leads else 0, 1)

    # Monthly trend: lead counts + won revenue (for charts)
    month_leads: dict[str, int] = defaultdict(int)
    month_won: dict[str, float] = defaultdict(float)
    for l in leads:
        ca = l.get("created_at")
        if not ca:
            continue
        try:
            dt = datetime.fromisoformat(str(ca).replace("Z", "+00:00"))
            key = dt.strftime("%Y-%m")
            month_leads[key] += 1
            if l.get("status") == "Won":
                month_won[key] += float(l.get("value") or 0)
        except Exception:
            pass

    months = sorted(set(month_leads.keys()) | set(month_won.keys()))[-6:]
    # If seed data clusters in few months, still show last 6 calendar months with zeros
    if len(months) < 2:
        from datetime import timezone
        now = datetime.now(timezone.utc)
        months = []
        for i in range(5, -1, -1):
            y = now.year
            m = now.month - i
            while m <= 0:
                m += 12
                y -= 1
            months.append(f"{y:04d}-{m:02d}")

    trend = [
        {
            "month": k,
            "leads": month_leads.get(k, 0),
            "count": month_leads.get(k, 0),  # alias
            "won": month_won.get(k, 0.0),
        }
        for k in months
    ]

    recent = sorted(leads, key=lambda x: x.get("updated_at") or "", reverse=True)[:5]
    recent_leads = [
        {
            "id": l["id"],
            "_id": l["id"],
            "name": l.get("name"),
            "company": l.get("company"),
            "status": l.get("status"),
            "value": float(l.get("value") or 0),
            "updatedAt": l.get("updated_at"),
            "updated_at": l.get("updated_at"),
        }
        for l in recent
    ]

    return {
        "success": True,
        "stats": {
            "revenueWon": won_value,
            "pipelineValue": total_value,
            "totalLeads": total_leads,
            "totalContacts": total_contacts,
            "openTasks": len([t for t in tasks if t.get("status") != "Completed"]),
            "conversionRate": conversion_rate,
        },
        "pipeline": [
            {"stage": s, "count": by_stage[s]["count"], "value": by_stage[s]["value"]}
            for s in LEAD_STAGES
        ],
        "trend": trend,
        "recentLeads": recent_leads,
    }
