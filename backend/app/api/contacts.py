from typing import Optional
from fastapi import APIRouter, HTTPException
from app.core.supabase_client import get_supabase
from app.api.deps import CurrentUser
from app.schemas.contact import (
    ContactCreate,
    ContactUpdate,
    ContactOut,
    ContactsResponse,
    ContactResponse,
)
from app.schemas.common import MessageResponse

router = APIRouter(prefix="/contacts", tags=["contacts"])


def _row_to_contact(row: dict) -> ContactOut:
    return ContactOut(
        id=row["id"],
        owner_id=row["owner_id"],
        name=row["name"],
        email=row.get("email") or "",
        phone=row.get("phone") or "",
        company=row.get("company") or "",
        title=row.get("title") or "",
        tags=row.get("tags") or [],
        notes=row.get("notes") or "",
        favorite=bool(row.get("favorite")),
        created_at=row.get("created_at"),
        updated_at=row.get("updated_at"),
    )


@router.get("", response_model=ContactsResponse)
async def get_contacts(
    current_user: CurrentUser,
    search: Optional[str] = None,
    tag: Optional[str] = None,
):
    supabase = get_supabase()
    q = supabase.table("contacts").select("*").eq("owner_id", current_user.id)
    if tag:
        q = q.contains("tags", [tag])
    res = q.order("favorite", desc=True).order("name").execute()
    contacts = [_row_to_contact(r) for r in (res.data or [])]
    if search:
        s = search.lower()
        contacts = [
            c
            for c in contacts
            if s in (c.name or "").lower()
            or s in (c.email or "").lower()
            or s in (c.phone or "").lower()
        ]
    return ContactsResponse(count=len(contacts), contacts=contacts)


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: str, current_user: CurrentUser):
    supabase = get_supabase()
    res = (
        supabase.table("contacts")
        .select("*")
        .eq("id", contact_id)
        .eq("owner_id", current_user.id)
        .single()
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Contact not found")
    return ContactResponse(contact=_row_to_contact(res.data))


@router.post("", response_model=ContactResponse, status_code=201)
async def create_contact(body: ContactCreate, current_user: CurrentUser):
    supabase = get_supabase()
    payload = body.model_dump()
    payload["owner_id"] = current_user.id
    res = supabase.table("contacts").insert(payload).execute()
    if not res.data:
        raise HTTPException(status_code=400, detail="Failed to create contact")
    return ContactResponse(contact=_row_to_contact(res.data[0]))


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: str, body: ContactUpdate, current_user: CurrentUser):
    supabase = get_supabase()
    updates = {k: v for k, v in body.model_dump(exclude_unset=True).items()}
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    res = (
        supabase.table("contacts")
        .update(updates)
        .eq("id", contact_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Contact not found")
    return ContactResponse(contact=_row_to_contact(res.data[0]))


@router.delete("/{contact_id}", response_model=MessageResponse)
async def delete_contact(contact_id: str, current_user: CurrentUser):
    supabase = get_supabase()
    res = (
        supabase.table("contacts")
        .delete()
        .eq("id", contact_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Contact not found")
    return MessageResponse(message="Contact deleted")
