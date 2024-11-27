import sqlite3
from typing import List, Tuple

class DatabaseManager:
    def __init__(self, db_name: str = 'npi_results.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self) -> None:
        """Initialize the database with required table"""
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS calculations(
                    id INTEGER PRIMARY KEY,
                    expression TEXT NOT NULL,
                    result REAL NOT NULL
                )
            """)
            conn.commit()

    def save_calculation(self, expression: str, result: float) -> None:
        """Save a calculation to the database
        
        Args:
            expression: The expression that was calculated
            result: The result of the calculation
        
        Returns:
            None
        """
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO calculations (expression, result) VALUES (?, ?)",
                (expression, result)
            )
            conn.commit()

    def get_all_calculations(self) -> List[Tuple]:
        """Get all calculations from the database
        
        Returns:
            List of tuples containing (id, expression, result)
        """
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM calculations")
            return cursor.fetchall()
        