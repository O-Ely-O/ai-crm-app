import os
import json
from typing import Any, Optional
from app.core.config import get_settings

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None


def is_ai_configured() -> bool:
    settings = get_settings()
    return bool(settings.GEMINI_API_KEY)


def _get_client():
    settings = get_settings()
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set")
    if genai is None:
        raise ValueError("google-genai package not installed")
    return genai.Client(api_key=settings.GEMINI_API_KEY)


def _generate_json(prompt: str, schema: dict) -> dict:
    client = _get_client()
    model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.6,
        ),
    )
    text = response.text or "{}"
    return json.loads(text)


def generate_lead_summary(lead: dict) -> dict:
    prompt = f"""You are an expert B2B sales analyst for a CRM called TTP CRM.
Analyze the following lead data and provide a concise summary.

Lead details:
- Name: {lead.get('name') or 'N/A'}
- Company: {lead.get('company') or 'N/A'}
- Email: {lead.get('email') or 'N/A'}
- Current pipeline stage: {lead.get('status') or 'New'}
- Potential deal value: ${lead.get('value') or 0}
- Source: {lead.get('source') or 'Unknown'}
- Notes: {lead.get('notes') or 'None'}

Return JSON only with keys: summary (string), riskScore (number 0-100), suggestedPriority (Low|Medium|High), nextBestAction (string)."""
    return _generate_json(prompt, {})


def generate_email(lead: dict, purpose: str = "follow-up", tone: str = "friendly and professional", sender: Optional[dict] = None) -> dict:
    sender = sender or {}
    prompt = f"""You are a senior sales rep writing on behalf of {sender.get('name') or 'the team'}{(' at ' + sender['company']) if sender.get('company') else ''}.

Write a professional sales email.
Purpose: {purpose}
Desired tone: {tone}

Recipient (lead) details:
- Name: {lead.get('name') or 'there'}
- Company: {lead.get('company') or 'N/A'}
- Pipeline stage: {lead.get('status') or 'New'}
- Context / notes: {lead.get('notes') or 'None'}

Return JSON only with keys: subject (string), body (string). Keep body under 180 words. Use \\n for line breaks."""
    return _generate_json(prompt, {})


def generate_sales_insights(pipeline_stats: Any) -> dict:
    prompt = f"""You are a revenue-operations advisor. Given this snapshot of a
sales pipeline, identify what is working, what is at risk, and concrete actions
to improve conversion.

Pipeline snapshot (JSON):
{json.dumps(pipeline_stats, default=str, indent=2)}

Return JSON only with keys: headline (string), insights (array of strings), recommendations (array of strings), healthScore (integer 0-100)."""
    return _generate_json(prompt, {})