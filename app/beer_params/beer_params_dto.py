from pydantic import BaseModel
from typing import Optional


class BeerParamInsertionDTO(BaseModel):
    name: str
    percentage_alcohol: float
    color: str
    type: str

    class Config:
        orm_mode = True  # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).


class BeerParamDTo(BeerParamInsertionDTO):
    id: int


class BeerParamUpdateDTO(BeerParamInsertionDTO):
    name: Optional[str]
    percentage_alcohol: Optional[float]
    color: Optional[str]
    type: Optional[str]
