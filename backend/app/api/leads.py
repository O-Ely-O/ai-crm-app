from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from app.core.supabase_client import get_supabase
from app.api.deps import CurrentUser
from app.schemas.lead import (
    LeadCreate,
    LeadUpdate,
    LeadOut,
    LeadReorderRequest,
    LeadsResponse,
    LeadResponse,
)
from app.schemas.common import MessageResponse

router = APIRouter(prefix="/leads", tags=["leads"])


def _row_to_lead(row: dict) -> LeadOut:
    return LeadOut(
        id=row["id"],
        owner_id=row["owner_id"],
        name=row["name"],
        email=row.get("email") or "",
        phone=row.get("phone") or "",
        company=row.get("company") or "",
        status=row.get("status") or "New",
        priority=row.get("priority") or "Medium",
        source=row.get("source") or "",
        value=float(row.get("value") or 0),
        notes=row.get("notes") or "",
        tags=row.get("tags") or [],
        ai_summary=row.get("ai_summary") or "",
        ai_risk_score=row.get("ai_risk_score"),
        order=row.get("order") or 0,
        created_at=row.get("created_at"),
        updated_at=row.get("updated_at"),
    )


@router.get("", response_model=LeadsResponse)
async def get_leads(
    current_user: CurrentUser,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    source: Optional[str] = None,
    search: Optional[str] = None,
):
    supabase = get_supabase()
    q = supabase.table("leads").select("*").eq("owner_id", current_user.id)
    if status:
        q = q.eq("status", status)
    if priority:
        q = q.eq("priority", priority)
    if source:
        q = q.eq("source", source)
    res = q.order("order").order("created_at", desc=True).execute()
    leads = [_row_to_lead(r) for r in (res.data or [])]
    if search:
        s = search.lower()
        leads = [
            l
            for l in leads
            if s in (l.name or "").lower()
            or s in (l.email or "").lower()
            or s in (l.company or "").lower()
        ]
    return LeadsResponse(leads=leads)


@router.get("/{lead_id}", response_model=LeadResponse)
async def get_lead(lead_id: str, current_user: CurrentUser):
    supabase = get_supabase()
    res = (
        supabase.table("leads")
        .select("*")
        .eq("id", lead_id)
        .eq("owner_id", current_user.id)
        .single()
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Lead not found")
    return LeadResponse(lead=_row_to_lead(res.data))


@router.post("", response_model=LeadResponse, status_code=201)
async def create_lead(body: LeadCreate, current_user: CurrentUser):
    supabase = get_supabase()
    payload = body.model_dump()
    payload["owner_id"] = current_user.id
    res = supabase.table("leads").insert(payload).execute()
    if not res.data:
        raise HTTPException(status_code=400, detail="Failed to create lead")
    return LeadResponse(lead=_row_to_lead(res.data[0]))


@router.put("/{lead_id}", response_model=LeadResponse)
async def update_lead(lead_id: str, body: LeadUpdate, current_user: CurrentUser):
    supabase = get_supabase()
    updates = {k: v for k, v in body.model_dump(exclude_unset=True).items()}
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    res = (
        supabase.table("leads")
        .update(updates)
        .eq("id", lead_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Lead not found")
    return LeadResponse(lead=_row_to_lead(res.data[0]))


@router.delete("/{lead_id}", response_model=MessageResponse)
async def delete_lead(lead_id: str, current_user: CurrentUser):
    supabase = get_supabase()
    res = (
        supabase.table("leads")
        .delete()
        .eq("id", lead_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Lead not found")
    return MessageResponse(message="Lead deleted successfully")


@router.patch("/reorder", response_model=MessageResponse)
async def reorder_leads(body: LeadReorderRequest, current_user: CurrentUser):
    supabase = get_supabase()
    for u in body.updates:
        supabase.table("leads").update(
            {"status": u.status, "order": u.order}
        ).eq("id", u.id).eq("owner_id", current_user.id).execute()
    return MessageResponse(message="Pipeline Updated")
