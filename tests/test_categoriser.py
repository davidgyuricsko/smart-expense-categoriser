import sys
from pathlib import Path

# Add /src to Python path so tests can import modules from there
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from categoriser import categorise_description


def test_food_and_drink():
    assert categorise_description("Starbucks") == "Food & Drink"
    assert categorise_description("Pret A Manger") == "Food & Drink"


def test_groceries():
    assert categorise_description("Tesco") == "Groceries"


def test_transport():
    assert categorise_description("Uber trip") == "Transport"
    assert categorise_description("Shell Petrol") == "Transport"


def test_income():
    assert categorise_description("Salary") == "Income"


def test_empty_description():
    assert categorise_description("") == "Uncategorised"
