from typing import Optional
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException
from app.core.supabase_client import get_supabase
from app.api.deps import CurrentUser
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskOut,
    TasksResponse,
    TaskResponse,
)
from app.schemas.common import MessageResponse

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _row_to_task(row: dict) -> TaskOut:
    return TaskOut(
        id=row["id"],
        owner_id=row["owner_id"],
        title=row["title"],
        description=row.get("description") or "",
        due_date=row.get("due_date"),
        status=row.get("status") or "Pending",
        priority=row.get("priority") or "Medium",
        related_lead_id=row.get("related_lead_id"),
        related_contact_id=row.get("related_contact_id"),
        completed_at=row.get("completed_at"),
        created_at=row.get("created_at"),
        updated_at=row.get("updated_at"),
        related_lead=row.get("related_lead"),
        related_contact=row.get("related_contact"),
    )


@router.get("", response_model=TasksResponse)
async def get_tasks(
    current_user: CurrentUser,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    related_lead: Optional[str] = None,
):
    supabase = get_supabase()
    q = (
        supabase.table("tasks")
        .select(
            "*, related_lead:leads(id, name, company), related_contact:contacts(id, name, company)"
        )
        .eq("owner_id", current_user.id)
    )
    if status:
        q = q.eq("status", status)
    if priority:
        q = q.eq("priority", priority)
    if related_lead:
        q = q.eq("related_lead_id", related_lead)
    res = q.order("due_date").order("created_at", desc=True).execute()
    tasks = [_row_to_task(r) for r in (res.data or [])]
    return TasksResponse(count=len(tasks), tasks=tasks)


@router.post("", response_model=TaskResponse, status_code=201)
async def create_task(body: TaskCreate, current_user: CurrentUser):
    supabase = get_supabase()
    payload = body.model_dump()
    payload["owner_id"] = current_user.id
    # Serialize datetime
    if payload.get("due_date"):
        payload["due_date"] = payload["due_date"].isoformat()
    res = supabase.table("tasks").insert(payload).execute()
    if not res.data:
        raise HTTPException(status_code=400, detail="Failed to create task")
    return TaskResponse(task=_row_to_task(res.data[0]))


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: str, body: TaskUpdate, current_user: CurrentUser):
    supabase = get_supabase()
    updates = {k: v for k, v in body.model_dump(exclude_unset=True).items()}
    if "due_date" in updates and updates["due_date"] is not None:
        updates["due_date"] = updates["due_date"].isoformat()
    if updates.get("status") == "Completed" and "completed_at" not in updates:
        updates["completed_at"] = datetime.now(timezone.utc).isoformat()
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    res = (
        supabase.table("tasks")
        .update(updates)
        .eq("id", task_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(task=_row_to_task(res.data[0]))


@router.delete("/{task_id}", response_model=MessageResponse)
async def delete_task(task_id: str, current_user: CurrentUser):
    supabase = get_supabase()
    res = (
        supabase.table("tasks")
        .delete()
        .eq("id", task_id)
        .eq("owner_id", current_user.id)
        .execute()
    )
    if not res.data:
        raise HTTPException(status_code=404, detail="Task not found")
    return MessageResponse(message="Task deleted successfully")
