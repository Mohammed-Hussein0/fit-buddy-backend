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