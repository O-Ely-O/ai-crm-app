from typing import Optional
from fastapi import APIRouter, HTTPException
from app.core.supabase_client import get_supabase
from app.api.deps import CurrentUser
from app.schemas.note import (
    NoteCreate,
    NoteUpdate,
    NoteOut,
    NotesResponse,
    NoteResponse,
)
from app.schemas.common import MessageResponse

router = APIRouter(prefix="/notes", tags=["notes"])


def _row_to_note(row: dict) -> NoteOut:
    return NoteOut(
        id=row["id"],
        owner_id=row["owner_id"],
        content=row["content"],
        lead_id=row.get("lead_id"),
        contact_id=row.get("contact_id"),
        pinned=bool(row.get("pinned")),
        created_at=row.get("created_at"),
        updated_at=row.get("updated_at"),
        lead=row.get("lead"),
        contact=row.get("contact"),
    )


@router.get("", response_model=NotesResponse)
async def get_notes(
    current_user: CurrentUser,
    lead: Optional[str] = None,
    contact: Optional[str] = None,
    search: Optional[str] = None,
):
    supabase = get_supabase()
    q = (
        supabase.table("notes")
        .select("*, lead:leads(id, name, company), contact:contacts(id, name, company)")
        .eq("owner_id", current_user.id)
    )
    if lead:
        q = q.eq("lead_id", lead)
    if contact:
        q = q.eq("contact_id", contact)
    res = q.order("created_at", desc=True).execute()
    notes = [_row_to_note(r) for r in (res.data or [])]
    if search:
        s = search.lower()
        notes = [n for n in notes if s in (n.content or "").lower()]
    return NotesResponse(count=len(notes), notes=notes)


@router.post("", response_model=NoteResponse, status_code=201)
async def create_note(body: NoteCreate, current_user: CurrentUser):
    if not body.content:
        raise HTTPException(status_code=400, detail="Content is required")
    supabase = get_supabase()
    payload = {
        "owner_id": current_user.id,
        "content": body.content,
        "lead_id": body.lead_id,
        "contact_id": body.contact_id,
        "pinned": body.pinned,
    }
    res = supabase.table("notes").insert(payload).execute()
    if not res.data:
        raise HTTPException(status_code=400, detail="Failed to create note")
    return NoteResponse(note=_row_to_note(res.data[0]))


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: str, body: NoteUpdate, current_user: CurrentUser):
    supabase = get_supabase()
    updates = {k: v for k, v in body.model_dump(exclude_unset=True).items()}
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    res = (
        supabase.table("notes")
        .update(updates)
        .eq("id", note_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(note=_row_to_note(res.data[0]))


@router.delete("/{note_id}", response_model=MessageResponse)
async def delete_note(note_id: str, current_user: CurrentUser):
    supabase = get_supabase()
    res = (
        supabase.table("notes")
        .delete()
        .eq("id", note_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Note not found")
    return MessageResponse(message="Note deleted successfully")
