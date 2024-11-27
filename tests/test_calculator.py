import pytest, sys, os

# Add the src directory to the Python path to import the calculator module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.calculator import calculate_npi

def test_basic_addition():
    assert calculate_npi("3 4 +") == 7.0

def test_basic_subtraction():
    assert calculate_npi("3 4 -") == -1.0

def test_basic_multiplication():
    assert calculate_npi("3 4 *") == 12.0

def test_basic_division():
    assert calculate_npi("12 3 /") == 4.0

def test_complex_expression():
    assert calculate_npi("3 4 + 5 *") == 35.0

def test_division_by_zero():
    assert calculate_npi("3 0 /") == float('inf')

def test_invalid_expression():
    with pytest.raises(ValueError):
        calculate_npi("3 + 4")

def test_empty_expression():
    with pytest.raises(ValueError, match="Empty expression"):
        calculate_npi("")

def test_single_number():
    assert calculate_npi("42") == 42.0

def test_not_enough_operands():
    with pytest.raises(ValueError, match="Not enough operands"):
        calculate_npi("3 +")
        
