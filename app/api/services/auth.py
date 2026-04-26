import os
import httpx
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from app.models.users import Users

SUPABASE_URL = os.getenv("SUPABASE_URL")
security = HTTPBearer()
_jwks = None

def get_jwks():
    global _jwks
    if _jwks is None:
        resp = httpx.get(f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json")
        resp.raise_for_status()
        _jwks = resp.json()
    return _jwks

def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            get_jwks(),
            algorithms=["ES256"],
            audience="authenticated"
        )
        return payload["sub"]
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))
        
def get_profile(db: Session, user_id: str):
    return db.execute(
        select(Users).where(Users.auth_id == user_id)
    ).scalar_one_or_none()