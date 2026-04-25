import enum

class GenderEnum(str, enum.Enum):
    MALE = 'male'
    FEMALE = 'female'

class HeightUnitEnum(str, enum.Enum):
    CM = 'cm'
    FEET = 'feet'

class SubscriptionPlanEnum(str, enum.Enum):
    FREE = 'free'
    PREMIUM = 'premium'


class ThemeEnum(str, enum.Enum):
    LIGHT = 'light'
    DARK = 'dark'


class WeightUnitEnum(str, enum.Enum):
    KG = 'kg'
    LBS = 'lbs'

class MuscleGroup(str, enum.Enum):
    chest      = "chest";      back       = "back"
    shoulders  = "shoulders";  biceps     = "biceps"
    triceps    = "triceps";    forearms   = "forearms"
    core       = "core";       glutes     = "glutes"
    quads      = "quads";      hamstrings = "hamstrings"
    calves     = "calves";     full_body  = "full_body"
    cardio     = "cardio"

class Equipment(str, enum.Enum):
    barbell    = "barbell";    dumbbell   = "dumbbell"
    cable      = "cable";      machine    = "machine"
    bodyweight = "bodyweight"; kettlebell = "kettlebell"
    bands      = "bands";      other      = "other"

class DifficultyLevel(str, enum.Enum):
    beginner     = "beginner"
    intermediate = "intermediate"
    advanced     = "advanced"

class PlanGoal(str, enum.Enum):
    strength    = "strength";   hypertrophy = "hypertrophy"
    endurance   = "endurance";  weight_loss = "weight_loss"
    maintenance = "maintenance"