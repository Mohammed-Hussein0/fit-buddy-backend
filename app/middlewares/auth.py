import requests
from fastapi import Header, HTTPException
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("PUBLIC_API_KEY")

def get_current_user_id(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = authorization.split(" ")[1]

    headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {token}"}
    resp = requests.get(f"{SUPABASE_URL}/auth/v1/user", headers=headers)
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid token")

    return resp.json()["id"]