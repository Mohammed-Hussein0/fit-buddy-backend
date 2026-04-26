# =============================================================================
# Workout Logging Router
# Prefix  : /workouts
# Tag     : Workouts
# Auth    : All routes require an authenticated user (get_current_user).
#
# Ownership rules:
#   - WorkoutPlans   : users can only read/modify plans where owner_id matches
#                      current_user.id. Plans where owner_id IS NULL are the
#                      official public plans — readable by everyone, not editable.
#   - WorkoutSessions: scoped strictly to current_user.id.
#   - WorkoutSets    : scoped through the parent session (which is already
#                      scoped to the user).
#
# Exercise selection:
#   When logging a WorkoutSet, the exercise_id may reference any row in the
#   exercises table (public, not user-scoped). Similarly, the optional plan_id
#   on a session may point to either the user's own plan or an official public
#   plan (owner_id IS NULL).
# =============================================================================

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

# from app.db.connection import get_db
# from app.dependencies.auth import get_current_user
# from app.models.users import Users
# from app.schemas.workout_plan import (
#     WorkoutPlanCreate, WorkoutPlanUpdate, WorkoutPlanResponse, WorkoutPlanListResponse,
#     WorkoutPlanExerciseCreate, WorkoutPlanExerciseUpdate, WorkoutPlanExerciseResponse,
# )
# from app.schemas.workout_session import (
#     WorkoutSessionCreate, WorkoutSessionUpdate, WorkoutSessionResponse, WorkoutSessionListResponse,
# )
# from app.schemas.workout_set import (
#     WorkoutSetCreate, WorkoutSetUpdate, WorkoutSetResponse,
# )

router = APIRouter(prefix="/workouts", tags=["Workouts"])


# =============================================================================
# WORKOUT PLANS
# Base path: /workouts/plans
# =============================================================================

# -----------------------------------------------------------------------------
# POST /workouts/plans
# Create a new personal workout plan for the authenticated user.
# Body  : WorkoutPlanCreate — name (required), description, goal,
#         duration_weeks, days_per_week.
# Note  : owner_id is set server-side from current_user.id (not from body).
# Returns: WorkoutPlanResponse.
# -----------------------------------------------------------------------------
# @router.post("/plans", response_model=WorkoutPlanResponse, status_code=status.HTTP_201_CREATED)
# async def create_plan(
#     payload: WorkoutPlanCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# GET /workouts/plans
# List all plans visible to the user: their own plans + official public plans
# (owner_id IS NULL). Useful for the "choose a plan" screen.
# Query params:
#   - skip       : int  (default 0)
#   - limit      : int  (default 20)
#   - owned_only : bool (default False) — return only the user's own plans
# Returns: WorkoutPlanListResponse.
# -----------------------------------------------------------------------------
# @router.get("/plans", response_model=WorkoutPlanListResponse)
# async def list_plans(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(20, ge=1, le=100),
#     owned_only: bool = Query(False),
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# GET /workouts/plans/{plan_id}
# Fetch a single plan with its exercises (WorkoutPlanExercise rows, ordered
# by day_order then position).
# Guard : 404 if not found. 403 if the plan is not public and not owned by user.
# Returns: WorkoutPlanResponse (with nested exercises).
# -----------------------------------------------------------------------------
# @router.get("/plans/{plan_id}", response_model=WorkoutPlanResponse)
# async def get_plan(
#     plan_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# PATCH /workouts/plans/{plan_id}
# Update a personal plan (partial update). Public plans (owner_id IS NULL)
# cannot be edited — return 403.
# Body  : WorkoutPlanUpdate — any subset of the writable fields.
# Guard : 404 / 403 if not owned by current_user.
# Note  : updated_at is maintained by a DB trigger, not set here.
# Returns: WorkoutPlanResponse.
# -----------------------------------------------------------------------------
# @router.patch("/plans/{plan_id}", response_model=WorkoutPlanResponse)
# async def update_plan(
#     plan_id: int,
#     payload: WorkoutPlanUpdate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# DELETE /workouts/plans/{plan_id}
# Delete a personal plan. Cascades to WorkoutPlanExercise rows.
# Public plans (owner_id IS NULL) cannot be deleted — return 403.
# Guard : 404 / 403 if not owned by current_user.
# Returns: 204 No Content.
# -----------------------------------------------------------------------------
# @router.delete("/plans/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_plan(
#     plan_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# =============================================================================
# WORKOUT PLAN EXERCISES
# Base path: /workouts/plans/{plan_id}/exercises
# Scoped under a plan — all routes first verify plan ownership.
# =============================================================================

# -----------------------------------------------------------------------------
# POST /workouts/plans/{plan_id}/exercises
# Add an exercise to a personal plan.
# Body  : WorkoutPlanExerciseCreate — exercise_id, day_order, position,
#         day_label, prescribed_sets, prescribed_reps, prescribed_rpe,
#         rest_seconds, notes.
# Guard : 409 if (plan_id, day_order, position) already exists (unique constraint).
# Returns: WorkoutPlanExerciseResponse.
# -----------------------------------------------------------------------------
# @router.post("/plans/{plan_id}/exercises", response_model=WorkoutPlanExerciseResponse, status_code=status.HTTP_201_CREATED)
# async def add_plan_exercise(
#     plan_id: int,
#     payload: WorkoutPlanExerciseCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# PATCH /workouts/plans/{plan_id}/exercises/{exercise_entry_id}
# Update a plan exercise entry (e.g. change prescribed sets/reps or reorder).
# Body  : WorkoutPlanExerciseUpdate — any subset of writable fields.
# Returns: WorkoutPlanExerciseResponse.
# -----------------------------------------------------------------------------
# @router.patch("/plans/{plan_id}/exercises/{exercise_entry_id}", response_model=WorkoutPlanExerciseResponse)
# async def update_plan_exercise(
#     plan_id: int,
#     exercise_entry_id: int,
#     payload: WorkoutPlanExerciseUpdate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# DELETE /workouts/plans/{plan_id}/exercises/{exercise_entry_id}
# Remove an exercise entry from a personal plan.
# Returns: 204 No Content.
# -----------------------------------------------------------------------------
# @router.delete("/plans/{plan_id}/exercises/{exercise_entry_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_plan_exercise(
#     plan_id: int,
#     exercise_entry_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# =============================================================================
# WORKOUT SESSIONS
# Base path: /workouts/sessions
# Scoped strictly to current_user.id.
# =============================================================================

# -----------------------------------------------------------------------------
# POST /workouts/sessions
# Start a new workout session.
# Body  : WorkoutSessionCreate — training_date (required), plan_id (optional,
#         may be user's own plan or a public plan), plan_day, notes.
# Note  : started_at defaults to now() server-side. ended_at is null until
#         the session is ended via PATCH.
# Returns: WorkoutSessionResponse.
# -----------------------------------------------------------------------------
# @router.post("/sessions", response_model=WorkoutSessionResponse, status_code=status.HTTP_201_CREATED)
# async def start_session(
#     payload: WorkoutSessionCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# PATCH /workouts/sessions/{session_id}/end
# End an active session by setting ended_at to now().
# Guard : 400 if session is already ended (ended_at is not null).
# Returns: WorkoutSessionResponse.
# -----------------------------------------------------------------------------
# @router.patch("/sessions/{session_id}/end", response_model=WorkoutSessionResponse)
# async def end_session(
#     session_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# GET /workouts/sessions
# List all sessions for the authenticated user, newest first.
# Query params:
#   - skip  : int (default 0)
#   - limit : int (default 20)
# Returns: WorkoutSessionListResponse.
# -----------------------------------------------------------------------------
# @router.get("/sessions", response_model=WorkoutSessionListResponse)
# async def list_sessions(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(20, ge=1, le=100),
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# GET /workouts/sessions/{session_id}
# Fetch a single session with all its logged sets.
# Guard : 404 / 403 as usual.
# Returns: WorkoutSessionResponse (with nested sets).
# -----------------------------------------------------------------------------
# @router.get("/sessions/{session_id}", response_model=WorkoutSessionResponse)
# async def get_session(
#     session_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# PATCH /workouts/sessions/{session_id}
# Update session metadata (notes, plan_id, plan_day, training_date).
# Does NOT set ended_at — use the /end endpoint for that.
# Returns: WorkoutSessionResponse.
# -----------------------------------------------------------------------------
# @router.patch("/sessions/{session_id}", response_model=WorkoutSessionResponse)
# async def update_session(
#     session_id: int,
#     payload: WorkoutSessionUpdate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# DELETE /workouts/sessions/{session_id}
# Delete a session and all its WorkoutSet children (cascade).
# Returns: 204 No Content.
# -----------------------------------------------------------------------------
# @router.delete("/sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_session(
#     session_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# =============================================================================
# WORKOUT SETS
# Base path: /workouts/sessions/{session_id}/sets
# Scoped under a session. Ownership is verified through the parent session.
# =============================================================================

# -----------------------------------------------------------------------------
# POST /workouts/sessions/{session_id}/sets
# Log a new set within an active session.
# Body  : WorkoutSetCreate — exercise_id (from exercises table, public),
#         set_number, weight_kg, reps, rpe, is_warmup, is_dropset,
#         is_failure, notes.
# Guard : 400 if the parent session is already ended.
#         404 if exercise_id doesn't exist in the exercises table.
# Note  : logged_at defaults to now().
# Returns: WorkoutSetResponse.
# -----------------------------------------------------------------------------
# @router.post("/sessions/{session_id}/sets", response_model=WorkoutSetResponse, status_code=status.HTTP_201_CREATED)
# async def log_set(
#     session_id: int,
#     payload: WorkoutSetCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# PATCH /workouts/sessions/{session_id}/sets/{set_id}
# Update a logged set (e.g. correct weight or reps after the fact).
# Body  : WorkoutSetUpdate — any subset of writable fields.
# Returns: WorkoutSetResponse.
# -----------------------------------------------------------------------------
# @router.patch("/sessions/{session_id}/sets/{set_id}", response_model=WorkoutSetResponse)
# async def update_set(
#     session_id: int,
#     set_id: int,
#     payload: WorkoutSetUpdate,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...


# -----------------------------------------------------------------------------
# DELETE /workouts/sessions/{session_id}/sets/{set_id}
# Remove a logged set from a session.
# Returns: 204 No Content.
# -----------------------------------------------------------------------------
# @router.delete("/sessions/{session_id}/sets/{set_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_set(
#     session_id: int,
#     set_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: Users = Depends(get_current_user),
# ):
#     ...