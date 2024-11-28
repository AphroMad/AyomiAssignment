import sqlite3
from typing import List, Tuple, Optional
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_name: str = 'npi_results.db'):
        self.db_name = db_name
        self.init_db()

    @contextmanager
    def get_connection(self):
        """
        Context manager for database connections.
        Handles connection lifecycle: connect -> commit/rollback -> close
        """
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise DatabaseError(f"Database operation failed: {str(e)}")
        finally:
            conn.close()

    def init_db(self) -> None:
        """
        Initializes database with required tables
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS calculations(
                    id INTEGER PRIMARY KEY,
                    expression TEXT NOT NULL,
                    result REAL NOT NULL
                )
            """)

    def save_calculation(self, expression: str, result: float) -> Optional[int]:
        """
        Saves calculation to database
        Returns: ID of inserted row or None if failed
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO calculations (expression, result) VALUES (?, ?)",
                    (expression, result)
                )
                return cursor.lastrowid
            except sqlite3.IntegrityError as e:
                raise DatabaseError(f"Failed to save calculation: {str(e)}")

    def get_all_calculations(self) -> List[Tuple]:
        """
        Retrieves all calculations from database
        Returns: List of tuples containing (id, expression, result)
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM calculations")
            return cursor.fetchall()

class DatabaseError(Exception):
    pass