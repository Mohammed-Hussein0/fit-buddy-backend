# =============================================================================
# Weight Logging Router
# Prefix  : /weights
# Tag     : Weight Logs
# Auth    : All routes require an authenticated user (get_current_user).
#           Every query is scoped to current_user.id — users can only
#           read and modify their own weight log entries.
# =============================================================================

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

# from app.db.connection import get_db
# from app.dependencies.auth import get_current_user
# from app.models.users import Users
# from app.schemas.weight import (
#     WeightLogCreate,
#     WeightLogUpdate,
#     WeightLogResponse,
#     WeightLogListResponse,
# )

router = APIRouter(prefix="/weights", tags=["Weight Logs"])


# -----------------------------------------------------------------------------
# POST /weights
# Log a new weight entry for the authenticated user.
# Body  : WeightLogCreate — weight_kg (required), body_fat_pct, muscle_mass_kg,
#         water_pct, visceral_fat, notes, logged_at (optional, defaults to now).
# Returns: WeightLogResponse (the created entry).
# -----------------------------------------------------------------------------
# @router.post("/", response_model=WeightLogResponse, status_code=status.HTTP_201_CREATED)
# async def log_weight(
#     payload: WeightLogCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# GET /weights
# Paginated list of the authenticated user's weight log entries.
# Query params:
#   - skip  : int  (default 0)  — offset for pagination
#   - limit : int  (default 20) — max entries to return
# Returns: WeightLogListResponse — list of entries + total count.
# -----------------------------------------------------------------------------
# @router.get("/", response_model=WeightLogListResponse)
# async def get_weight_logs(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(20, ge=1, le=100),
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# GET /weights/{log_id}
# Fetch a single weight log entry by ID.
# Path  : log_id (BigInteger) — the ID of the weight log entry.
# Guard : 404 if not found, 403 if entry doesn't belong to current_user.
# Returns: WeightLogResponse.
# -----------------------------------------------------------------------------
# @router.get("/{log_id}", response_model=WeightLogResponse)
# async def get_weight_log(
#     log_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# PATCH /weights/{log_id}
# Update a weight log entry (partial update).
# Path  : log_id — the entry to update.
# Body  : WeightLogUpdate — any subset of the writable fields.
# Guard : 404 if not found, 403 if not owned by current_user.
# Returns: WeightLogResponse (updated entry).
# -----------------------------------------------------------------------------
# @router.patch("/{log_id}", response_model=WeightLogResponse)
# async def update_weight_log(
#     log_id: int,
#     payload: WeightLogUpdate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# DELETE /weights/{log_id}
# Delete a weight log entry.
# Path  : log_id — the entry to delete.
# Guard : 404 if not found, 403 if not owned by current_user.
# Returns: 204 No Content.
# -----------------------------------------------------------------------------
# @router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_weight_log(
#     log_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...