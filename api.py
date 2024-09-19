from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional

# Initialize the APIRouter
router = APIRouter()

# Predefined items
items = [
    {"trade": "Earthworks", "unit_of_measure": "M3", "rate": 50.0},
    {"trade": "Concrete", "unit_of_measure": "M3", "rate": 120.0},
    {"trade": "Bricklaying", "unit_of_measure": "M2", "rate": 75.0},
    {"trade": "Carpentry", "unit_of_measure": "LM", "rate": 30.0},
    {"trade": "Carpentry", "unit_of_measure": "HOURS", "rate": 60.0},
    {"trade": "Carpentry", "unit_of_measure": "M2", "rate": 60.0},
    {"trade": "Carpentry", "unit_of_measure": "EACH", "rate": 100.0},
    {"trade": "Roofing", "unit_of_measure": "M2", "rate": 90.0},
    {"trade": "Electrical", "unit_of_measure": "EACH", "rate": 45.0},
    {"trade": "Plumbing", "unit_of_measure": "EACH", "rate": 150.0},
    {"trade": "Plastering", "unit_of_measure": "M2", "rate": 25.0},
    {"trade": "Painting", "unit_of_measure": "M2", "rate": 23.0},
    {"trade": "Painting", "unit_of_measure": "LM", "rate": 16.0},
    {"trade": "Painting", "unit_of_measure": "HOURS", "rate": 55.0},
    {"trade": "Joinery", "unit_of_measure": "EACH", "rate": 200.0},
]


# Pydantic model for the request
class ItemRequest(BaseModel):
    trade: Optional[str] = Field(None, description="The trade to search for")
    unit_of_measure: Optional[str] = Field(
        None, description="The unit of measure to search for"
    )


# Pydantice model for the response
class ItemDetails(BaseModel):
    trade: str
    unit_of_measure: str
    rate: float


class MatchResponse(BaseModel):
    best_match: ItemDetails
    similarity_score: float


# API endpoint to return all the items
@router.get("/items")
def get_items():
    return items
