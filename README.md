# Matching Algorithm API

A FastAPI application that provides a RESTful API for matching user input against a predefined list of items and returning the best match along with a similarity score.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sarmaakondi/matching-algo-api.git
cd matching-algo-api
```

### 2. Create a Virtual Environment

Using `venv`:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

-   On Windows:

    ```bash
    .venv\Scripts\activate
    ```

-   On macOS/Linux:

    ```bash
    source .venv/bin/activate
    ```

### 4. Install Requirements

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Run the FastAPI Application

-   Old Method

    ```bash
    uvicorn main:app --reload
    ```

-   New Method

    ```bash
    fastapi dev main.py
    ```

-   The application will be available at `http://127.0.0.1:8000`
-   The docs/api-ednpoints will be available at `http://127.0.0.1:8000/docs`

### 6. Run Tests

-   To run the test cases, use `pytest`:

    ```bash
    pytest
    ```

-   If you encounter issues with the `pytest` command, you can use the following fallback command. This sets the `PYTHONPATH` environment variable to the current directory and then runs `pytest`.

    ```bash
    PYTHONPATH=./ pytest
    ```

## Endpoints

```
GET /api/items
```

Returns the list of predefined items.

```
POST /api/match
```

Matches the provided input with the predefined list of items and returns the best match along with a similarity score.

### Request Body Example:

```bash
{
  "trade": "painting",
  "unit_of_measure": "m2"
}
```

### Response Example:

```bash
{
  "best_match": {
    "trade": "Painting",
    "unit_of_measure": "M2",
    "rate": 23.0
  },
  "similarity_score": 0.75
}
```

## Error Handling

-   400 Bad Request: `'trade' and 'unit_of_measure' cannot be empty.`
-   404 Not Found: `No matching item found for the provided input.`
