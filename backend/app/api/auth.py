from fastapi import APIRouter, HTTPException, status
from app.core.supabase_client import get_supabase
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserOut,
    AuthResponse,
)
from app.api.deps import CurrentUser

router = APIRouter(prefix="/auth", tags=["auth"])


def _to_user_out(data: dict) -> UserOut:
    return UserOut(
        id=data["id"],
        name=data["name"],
        email=data["email"],
        role=data.get("role", "member"),
        company=data.get("company") or "",
        avatar=data.get("avatar") or "",
        created_at=data.get("created_at"),
        updated_at=data.get("updated_at"),
    )


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(body: UserCreate):
    supabase = get_supabase()
    try:
        # Sign up via Supabase Auth
        auth_res = supabase.auth.sign_up(
            {
                "email": body.email.lower(),
                "password": body.password,
                "options": {
                    "data": {
                        "name": body.name,
                        "company": body.company or "",
                        "role": "member",
                    }
                },
            }
        )
        if not auth_res.user:
            raise HTTPException(status_code=400, detail="Registration failed")
        session = auth_res.session
        token = session.access_token if session else ""
        # Profile is created by trigger; fetch it
        profile = (
            supabase.table("profiles")
            .select("*")
            .eq("id", auth_res.user.id)
            .single()
            .execute()
        )
        if not profile.data:
            # Fallback if trigger lag
            supabase.table("profiles").upsert(
                {
                    "id": auth_res.user.id,
                    "name": body.name,
                    "email": body.email.lower(),
                    "company": body.company or "",
                    "role": "member",
                }
            ).execute()
            profile = (
                supabase.table("profiles")
                .select("*")
                .eq("id", auth_res.user.id)
                .single()
                .execute()
            )
        return AuthResponse(token=token, user=_to_user_out(profile.data))
    except HTTPException:
        raise
    except Exception as e:
        msg = str(e)
        if "already registered" in msg.lower() or "already been registered" in msg.lower():
            raise HTTPException(status_code=409, detail="Email already in use")
        raise HTTPException(status_code=400, detail=msg)


@router.post("/login", response_model=AuthResponse)
async def login(body: UserLogin):
    supabase = get_supabase()
    try:
        auth_res = supabase.auth.sign_in_with_password(
            {"email": body.email.lower(), "password": body.password}
        )
        if not auth_res.user or not auth_res.session:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        profile = (
            supabase.table("profiles")
            .select("*")
            .eq("id", auth_res.user.id)
            .single()
            .execute()
        )
        if not profile.data:
            raise HTTPException(status_code=401, detail="User profile not found")
        return AuthResponse(
            token=auth_res.session.access_token,
            user=_to_user_out(profile.data),
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid email or password")


@router.get("/me")
async def get_me(current_user: CurrentUser):
    return {"success": True, "user": current_user}


@router.put("/profile")
async def update_profile(body: UserUpdate, current_user: CurrentUser):
    supabase = get_supabase()
    updates = {}
    if body.name is not None:
        updates["name"] = body.name
    if body.company is not None:
        updates["company"] = body.company
    if body.avatar is not None:
        updates["avatar"] = body.avatar
    if not updates and body.password is None:
        raise HTTPException(status_code=400, detail="No fields to update")
    if updates:
        res = (
            supabase.table("profiles")
            .update(updates)
            .eq("id", current_user.id)
            .execute()
        )
        if not res.data:
            raise HTTPException(status_code=404, detail="User not found")
        data = res.data[0]
    else:
        data = {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email,
            "role": current_user.role,
            "company": current_user.company,
            "avatar": current_user.avatar,
            "created_at": current_user.created_at,
            "updated_at": current_user.updated_at,
        }
    if body.password:
        # Update password via admin or user update
        try:
            supabase.auth.admin.update_user_by_id(
                current_user.id, {"password": body.password}
            )
        except Exception:
            pass  # may require service role
    return {"success": True, "user": _to_user_out(data)}
