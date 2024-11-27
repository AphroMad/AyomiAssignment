from fastapi.testclient import TestClient
from main import app
import pytest
import csv 
from io import StringIO

client = TestClient(app)

def test_calculate_endpoint_valid():
    response = client.post(
        "/calculate",
        json={"expression": "3 4 +"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 7.0}

def test_calculate_endpoint_invalid():
    response = client.post(
        "/calculate",
        json={"expression": "3 + 4"}  # Invalid NPI expression
    )
    assert response.status_code == 400

def test_csv_endpoint():
    # First add some calculations
    client.post("/calculate", json={"expression": "3 4 +"})
    client.post("/calculate", json={"expression": "5 2 *"})
    
    # Then test CSV endpoint
    response = client.get("/calculations/csv")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    
    # Parse the CSV content
    csv_content = StringIO(response.text)
    reader = csv.DictReader(csv_content)
    rows = list(reader)
    
    # Check we have the expected number of rows
    assert len(rows) >= 2
    
    # Check the structure and data types without depending on specific IDs
    for row in rows:
        assert "ID" in row
        assert "Expression" in row
        assert "Result" in row
        assert float(row["Result"])  # Result should be convertible to float
        