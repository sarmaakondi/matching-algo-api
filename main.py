from fastapi import FastAPI
from api import router

# Initialize the FastAPI app instance
app = FastAPI(
    title="Matching Algorithm API",
    description="A RESTful API that takes user input, attempt to match it against a predefined list of items and return the best match along with a similarity score.",
    version="0.1.0",
)

# Include the router in the app instance
app.include_router(router, prefix="/api", tags=["Matching API"])


# Root endpoint
@app.get("/", tags=["Root API"])
def root():
    return {"message": "Hello from FastAPI 😁"}
