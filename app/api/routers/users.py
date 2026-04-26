from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.connection import get_db
from app.models.users import Users
from app.api.schemas.users import UserProfileUpdate, UserProfileResponse, UserProfileCreate
from app.api.services.auth import get_current_user_id, get_profile

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/profile", response_model=UserProfileResponse, status_code=201)
def create_profile(
    payload: UserProfileCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    
    profile = get_profile(db, user_id)

    if profile:
        raise HTTPException(
            status_code=400, detail="Profile already exists for this user"
        )

    new_profile = Users(
        auth_id=user_id,
        **payload.model_dump()
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile

###########################################################################################################

@router.patch("/profile", response_model=UserProfileResponse, status_code=200)
def update_profile(
    payload: UserProfileUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    profile = get_profile(db, user_id)

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile

###########################################################################################################

@router.get("/profile", response_model=UserProfileResponse, status_code=200)
def get_profile(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    profile = get_profile(db, user_id)

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile