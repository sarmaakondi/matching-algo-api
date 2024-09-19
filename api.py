from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from difflib import SequenceMatcher

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
    trade: Optional[str] = Field(None)
    unit_of_measure: Optional[str] = Field(None)


# Pydantic model for the response
class ItemDetails(BaseModel):
    trade: str
    unit_of_measure: str
    rate: float


class MatchResponse(BaseModel):
    best_match: ItemDetails
    similarity_score: float


# Helper function to calculate the similarity score
def calculate_similarity(input_str: str, item_str: str) -> float:
    return SequenceMatcher(None, input_str, item_str).ratio()


# API endpoint to return all the items
@router.get("/items")
def get_items():
    return items


# API endpoint to match an item based on the user input
@router.post("/match", response_model=MatchResponse)
def match_item(request: ItemRequest):
    # Validate input
    if not request.trade or not request.unit_of_measure:
        raise HTTPException(
            status_code=400,
            detail="'trade' and 'unit_of_measure' cannot be empty.",
        )

    # Calculate the similarity score
    best_match = None
    best_score = 0.0
    input_trade_str = request.trade.lower()
    input_uom_str = request.unit_of_measure.lower()

    for item in items:
        item_trade_str = item["trade"].lower()
        item_uom_str = item["unit_of_measure"].lower()
        trade_score = calculate_similarity(input_trade_str, item_trade_str)
        uom_score = calculate_similarity(input_uom_str, item_uom_str)

        average_score = (trade_score + uom_score) / 2

        if average_score > best_score:
            best_score = average_score
            best_match = item

    # Response based on similarity threshold and best_match
    similarity_threshold = 0.38
    if best_match is None or best_score < similarity_threshold:
        raise HTTPException(
            status_code=404,
            detail="No matching item found for the provided input.",
        )

    # Return matched item details
    return MatchResponse(
        best_match=ItemDetails(**best_match),
        similarity_score=f"{best_score:.2f}",
    )
