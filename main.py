from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import csv
from io import StringIO

from src.calculator import calculate_npi
from src.db.operations import DatabaseManager, DatabaseError


app = FastAPI()
db = DatabaseManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NPIExpression(BaseModel):
    expression: str


@app.post("/calculate")
def calculate_expression(expression: NPIExpression):
    try:
        result = calculate_npi(expression.expression)
        row_id = db.save_calculation(expression.expression, result)
        if not row_id:
            raise HTTPException(status_code=500, detail="Failed to save calculation")
        return {"result": result, "id": row_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {str(e)}")
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    
@app.get("/calculations/csv")
def export_calculations():
    try : 
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
        
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/calculations")
def get_calculations():
    try:
        calculations = db.get_all_calculations()
        return [{"expression": calc[1], "result": calc[2]} for calc in calculations]
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    