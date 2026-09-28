from typing import Optional, Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.api.deps import CurrentUser
from app.services import ai_service
from app.core.supabase_client import get_supabase

router = APIRouter(prefix="/ai", tags=["ai"])


class LeadSummaryRequest(BaseModel):
    lead_id: Optional[str] = None
    lead: Optional[dict] = None


class EmailRequest(BaseModel):
    lead_id: Optional[str] = None
    lead: Optional[dict] = None
    purpose: str = "follow-up"
    tone: str = "friendly and professional"


class InsightsRequest(BaseModel):
    pipeline_stats: Optional[Any] = None


@router.get("/status")
async def ai_status():
    return {
        "success": True,
        "configured": ai_service.is_ai_configured(),
    }


@router.post("/lead-summary")
async def lead_summary(body: LeadSummaryRequest, current_user: CurrentUser):
    if not ai_service.is_ai_configured():
        raise HTTPException(status_code=503, detail="AI is not configured")
    lead = body.lead
    if body.lead_id and not lead:
        supabase = get_supabase()
        res = (
            supabase.table("leads")
            .select("*")
            .eq("id", body.lead_id)
            .eq("owner_id", current_user.id)
            .single()
            .execute()
        )
        if not res.data:
            raise HTTPException(status_code=404, detail="Lead not found")
        lead = res.data
    if not lead:
        raise HTTPException(status_code=400, detail="lead or lead_id required")
    try:
        result = ai_service.generate_lead_summary(lead)
        # Optionally persist summary
        if body.lead_id and result.get("summary"):
            supabase = get_supabase()
            supabase.table("leads").update(
                {
                    "ai_summary": result.get("summary"),
                    "ai_risk_score": result.get("riskScore"),
                }
            ).eq("id", body.lead_id).eq("owner_id", current_user.id).execute()
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI request failed: {str(e)}")


@router.post("/email")
async def generate_email(body: EmailRequest, current_user: CurrentUser):
    if not ai_service.is_ai_configured():
        raise HTTPException(status_code=503, detail="AI is not configured")
    lead = body.lead
    if body.lead_id and not lead:
        supabase = get_supabase()
        res = (
            supabase.table("leads")
            .select("*")
            .eq("id", body.lead_id)
            .eq("owner_id", current_user.id)
            .single()
            .execute()
        )
        if not res.data:
            raise HTTPException(status_code=404, detail="Lead not found")
        lead = res.data
    if not lead:
        raise HTTPException(status_code=400, detail="lead or lead_id required")
    try:
        result = ai_service.generate_email(
            lead,
            purpose=body.purpose,
            tone=body.tone,
            sender={"name": current_user.name, "company": current_user.company},
        )
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI request failed: {str(e)}")


@router.post("/insights")
async def sales_insights(body: InsightsRequest, current_user: CurrentUser):
    if not ai_service.is_ai_configured():
        raise HTTPException(status_code=503, detail="AI is not configured")
    stats = body.pipeline_stats
    if not stats:
        # Fetch basic pipeline
        supabase = get_supabase()
        leads = (
            supabase.table("leads")
            .select("status, value")
            .eq("owner_id", current_user.id)
            .execute()
        )
        stats = leads.data or []
    try:
        result = ai_service.generate_sales_insights(stats)
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI request failed: {str(e)}")
