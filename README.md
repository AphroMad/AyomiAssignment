# AyomiAssignment
Calculatrice en notation polonaise inverse (NPI) avec interface web

## Backend Setup

1. Clone repository
2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Local Development
```bash
uvicorn main:app --reload
```

### Production (Docker)
```bash
docker compose up --build
```

## Frontend Setup

1. Install Node.js and npm
2. Create React app and install dependencies:
```bash
npx create-react-app npi-calculator
cd npi-calculator
npm install
```

3. Copy provided components into `src/components/`
4. Start development server:
```bash
npm start
```

## Project Structure
```
├── backend/
│   ├── main.py
│   ├── src/
│   │   ├── calculator.py
│   │   └── db/
│   │       └── operations.py
│   └── tests/
└── frontend/
    └── src/
        └── components/
            ├── Calculator/
            ├── ProgressBar/
            ├── CalculatorInput/
            └── HistoryList/
```

## Available Endpoints

- `POST /calculate`: Calculate NPI expression
```json
{
  "expression": "3 4 +"
}
```
- `GET /calculations`: Get calculation history
- `GET /calculations/csv`: Download CSV

## API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

### Backend Tests
```bash
pytest tests/
```

### API Testing
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"expression": "3 4 +"}' \
     'http://localhost:8000/calculate'
```

## Resources

- [FastAPI Tutorial](https://www.youtube.com/watch?v=iWS9ogMPOI0)
- [SQLite Tutorial](https://www.youtube.com/watch?v=girsuXz0yA8)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
