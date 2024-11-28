import pytest
from src.db.operations import DatabaseManager, DatabaseError
import os

@pytest.fixture
def db_manager():
    # Use a test database file
    test_db = "test_npi_results.db"
    db = DatabaseManager(test_db)
    yield db
    # Cleanup after tests
    if os.path.exists(test_db):
        os.remove(test_db)

def test_save_calculation(db_manager):
    db_manager.save_calculation("3 4 +", 7.0)
    calculations = db_manager.get_all_calculations()
    assert len(calculations) == 1
    assert calculations[0][1] == "3 4 +"  # expression
    assert calculations[0][2] == 7.0      # result

def test_get_all_calculations(db_manager):
    db_manager.save_calculation("3 4 +", 7.0)
    db_manager.save_calculation("5 2 *", 10.0)
    calculations = db_manager.get_all_calculations()
    assert len(calculations) == 2
    
def test_database_error(db_manager):
    with pytest.raises(DatabaseError):
        # Force error by passing invalid types
        db_manager.save_calculation(None, None)
        