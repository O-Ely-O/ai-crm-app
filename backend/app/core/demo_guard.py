"""Cap how many rows the shared demo account can create."""
from fastapi import HTTPException
from app.core.config import get_settings
from app.core.supabase_client import get_supabase


def _is_demo_email(email: str) -> bool:
    settings = get_settings()
    return (email or "").strip().lower() == settings.DEMO_EMAIL.strip().lower()


def enforce_demo_create_cap(user_email: str, user_id: str, table: str) -> None:
    settings = get_settings()
    if not _is_demo_email(user_email):
        return

    caps = {
        "leads": settings.DEMO_MAX_LEADS,
        "contacts": settings.DEMO_MAX_CONTACTS,
        "notes": settings.DEMO_MAX_NOTES,
        "tasks": settings.DEMO_MAX_TASKS,
    }
    cap = caps.get(table)
    if cap is None:
        return

    supabase = get_supabase()
    res = (
        supabase.table(table)
        .select("id", count="exact")
        .eq("owner_id", user_id)
        .limit(1)
        .execute()
    )
    count = res.count if res.count is not None else 0
    if count >= cap:
        raise HTTPException(
            status_code=403,
            detail=(
                f"Demo account limit reached ({cap} {table}). "
                "Data resets periodically — please explore without flooding the demo."
            ),
        )
