from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.supabase_client import get_supabase
from app.schemas.user import UserOut

security = HTTPBearer()


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> UserOut:
    token = credentials.credentials
    supabase = get_supabase()
    try:
        # Verify token via Supabase Auth
        user_response = supabase.auth.get_user(token)
        if not user_response or not user_response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authorized, invalid token",
            )
        auth_user = user_response.user
        # Fetch profile
        profile = (
            supabase.table("profiles")
            .select("*")
            .eq("id", auth_user.id)
            .single()
            .execute()
        )
        if not profile.data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authorized, user not found",
            )
        data = profile.data
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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Not authorized: {str(e)}",
        )


CurrentUser = Annotated[UserOut, Depends(get_current_user)]