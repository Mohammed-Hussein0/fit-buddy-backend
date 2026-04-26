from decimal import Decimal
from typing import Annotated

from pydantic import Field

HeightType   = Annotated[Decimal, Field(gt=0, max_digits=4, decimal_places=1)]
WeightType   = Annotated[Decimal, Field(gt=0, max_digits=5, decimal_places=2)]
UsernameType = Annotated[str,     Field(min_length=3, max_length=20)]
