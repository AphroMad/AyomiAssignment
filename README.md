# AyomiAssignment
Création d'une calculatrice en notation polonaise inverse (NPI)

## Setup and Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development
```bash
uvicorn main:app --reload
```

### Using Docker
```bash
docker-compose up --build  # Build and start
docker-compose up         # Start
docker-compose down       # Stop
docker-compose down --volumes  # Clean start (including database)
```

## Testing the Application

```bash
# Calculate first expression
curl -X POST -H "Content-Type: application/json" -d '{"expression": "3 4 +"}' 'http://localhost:8000/calculate'

# Calculate second expression
curl -X POST -H "Content-Type: application/json" -d '{"expression": "5 2 *"}' 'http://localhost:8000/calculate'

# Get all calculations in CSV format
curl "http://localhost:8000/calculations/csv" --output calculations.csv
```

## API Testing

### Console Testing
```bash
# GET request
curl -X GET http://127.0.0.1:8000/endpoint_you_want

# Simple POST request
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/endpoint?value=test'

# POST request with JSON body
curl -X POST -H "Content-Type: application/json" -d '{"expression": "3 4 +"}' 'http://127.0.0.1:8000/calculate'
```

### API Documentation
Automatic documentation and testing interfaces available at:
- Swagger UI: `http://127.0.0.1:8000/docs#/`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Available Endpoints
- `POST /calculate`: Calculate NPI expression
  ```json
  {
    "expression": "3 4 +"
  }
  ```
- `GET /calculations/csv`: Download all calculations as CSV

### Understanding HTTP Status Codes
For error messages reference: [Mozilla HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Resources

### FastAPI
Learn how to use FastAPI to create a simple REST API:
- Tutorial: [FastAPI Tutorial](https://www.youtube.com/watch?v=iWS9ogMPOI0)

### SQLite 3
Learn how to use SQLite 3 to create simple DB:
- Tutorial: [SQLite Tutorial](https://www.youtube.com/watch?v=girsuXz0yA8)
