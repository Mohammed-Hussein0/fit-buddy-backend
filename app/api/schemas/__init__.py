# schemas/__init__.py
# Re-exports everything so routers can do:
#   from app.schemas import WeightLogCreate, WorkoutSetResponse, ...
# instead of importing from individual sub-modules.

from .common import HeightType, WeightType, UsernameType

from .user import (
    UserProfileCreate,
    UserProfileUpdate,
    UserProfileResponse,
)

from .weight import (
    WeightLogBase,
    WeightLogCreate,
    WeightLogUpdate,
    WeightLogResponse,
    WeightLogListResponse,
)

from .workout_set import (
    WorkoutSetBase,
    WorkoutSetCreate,
    WorkoutSetUpdate,
    WorkoutSetResponse,
)

from .workout_session import (
    WorkoutSessionBase,
    WorkoutSessionCreate,
    WorkoutSessionUpdate,
    WorkoutSessionResponse,
    WorkoutSessionListResponse,
)

from .workout_plan import (
    WorkoutPlanExerciseBase,
    WorkoutPlanExerciseCreate,
    WorkoutPlanExerciseUpdate,
    WorkoutPlanExerciseResponse,
    WorkoutPlanBase,
    WorkoutPlanCreate,
    WorkoutPlanUpdate,
    WorkoutPlanResponse,
    WorkoutPlanListResponse,
)

from .catalogue import (
    ExerciseResponse,
    ExerciseListResponse,
    OfficialPlanExerciseResponse,
    OfficialPlanResponse,
    OfficialPlanListResponse,
)

__all__ = [
    # Common annotated types
    "HeightType", "WeightType", "UsernameType",
    # User
    "UserProfileCreate", "UserProfileUpdate", "UserProfileResponse",
    # Weight
    "WeightLogBase", "WeightLogCreate", "WeightLogUpdate",
    "WeightLogResponse", "WeightLogListResponse",
    # Workout Set
    "WorkoutSetBase", "WorkoutSetCreate", "WorkoutSetUpdate", "WorkoutSetResponse",
    # Workout Session
    "WorkoutSessionBase", "WorkoutSessionCreate", "WorkoutSessionUpdate",
    "WorkoutSessionResponse", "WorkoutSessionListResponse",
    # Workout Plan & Plan Exercise
    "WorkoutPlanExerciseBase", "WorkoutPlanExerciseCreate", "WorkoutPlanExerciseUpdate",
    "WorkoutPlanExerciseResponse",
    "WorkoutPlanBase", "WorkoutPlanCreate", "WorkoutPlanUpdate",
    "WorkoutPlanResponse", "WorkoutPlanListResponse",
    # Catalogue (read-only)
    "ExerciseResponse", "ExerciseListResponse",
    "OfficialPlanExerciseResponse", "OfficialPlanResponse", "OfficialPlanListResponse",
]