from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.config.db import get_db
from app.api.v1.users.models import UserProfile
from app.api.v1.users.schemas import UserProfileUpdate, UserProfileResponse, UserProfileCreate
from app.middlewares.auth import get_current_user_id

router = APIRouter()

@router.post("/users/profile", response_model=UserProfileResponse)
def create_my_profile(
    payload: UserProfileCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    # Check if the user already has a profile
    existing_profile = db.execute(
        select(UserProfile).where(UserProfile.auth_id == user_id)
    ).scalar_one_or_none()

    if existing_profile:
        raise HTTPException(
            status_code=400, detail="Profile already exists for this user"
        )

    # Create new profile
    new_profile = UserProfile(
        auth_id=user_id,
        **payload.model_dump()
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile

###########################################################################################################

@router.put("/users/profile", response_model=UserProfileResponse)
def update_my_profile(
    payload: UserProfileUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    profile = db.execute(
        select(UserProfile).where(UserProfile.auth_id == user_id)
    ).scalar_one_or_none()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile

###########################################################################################################

@router.get("/users/profile", response_model=UserProfileResponse)
def update_my_profile(
    payload: UserProfileResponse,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    profile = db.execute(
        select(UserProfile).where(UserProfile.auth_id == user_id)
    ).scalar_one_or_none()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile