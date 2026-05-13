from pydantic import BaseModel

# This class defines the "shape" of a Coin object
class Coin(BaseModel):
    # Unique identifier of the coin
    id: str

    # Short symbol of the coin
    symbol: str

    # Full readable name of the coin
    name: str