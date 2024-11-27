from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import csv
from io import StringIO

from src.calculator import calculate_npi
from src.db.operations import DatabaseManager


app = FastAPI()
db = DatabaseManager()


class NPIExpression(BaseModel):
    expression: str


@app.post("/calculate")
def calculate_expression(expression: NPIExpression):
    try:
        # Calculate result
        result = calculate_npi(expression.expression)
        
        # Store in database
        db.save_calculation(expression.expression, result)
        
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@app.get("/calculations/csv")
def export_calculations():
    # Get all calculations from database
    calculations = db.get_all_calculations()
    
    # Create CSV in memory
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(["ID", "Expression", "Result"])
    
    # Write data
    for calc in calculations:
        writer.writerow(calc)
    
    # Prepare response
    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=calculations.csv"
        }
    )
