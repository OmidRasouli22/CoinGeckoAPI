from pydantic import BaseModel, Field, validator
import re


class CoinModel(BaseModel):
    """
    This model is used to validate raw API data from CoinGecko.

    It ensures the data is clean before entering the system.
    """

    id: str = Field(..., min_length=1)
    symbol: str = Field(..., min_length=1, max_length=20)
    name: str = Field(..., min_length=1)

    @validator("id")
    def validate_id(cls, v):
        if not re.match(r"^[a-zA-Z0-9\-]+$", v):
            raise ValueError("Invalid coin id format")
        return v