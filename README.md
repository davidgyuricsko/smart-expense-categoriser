# Smart Expense Categoriser

A Python application that analyses personal expense transactions from CSV files, categorises them using rule-based logic, and generates clear category-based spending summaries.

This project focuses on clean structure, predictable behaviour, and testability rather than machine learning or overengineering.

---

## Features
- Load transactions from CSV files
- Automatically categorise expenses using keyword-based rules
- Separate income from spending
- Generate category-level spending totals
- Includes automated unit tests with pytest

---

## Example Output
The application outputs:
- A table of transactions with an added `category` column
- A summary of total spending grouped by category (income excluded)

---

## Project Structure
- `src/`
  - `loader.py` — CSV loading
  - `categoriser.py` — Category rules and logic
  - `summariser.py` — Data enrichment and aggregation
  - `main.py` — Application entry point
- `tests/`
  - `test_categoriser.py` — Unit tests for categorisation
- `data/`
  - `sample_transactions.csv` — Example input data
- `requirements.txt` — Dependencies
- `README.md` — Project documentation


---

## How It Works
1. Transactions are loaded into a pandas DataFrame
2. Each transaction description is matched against keyword-based category rules
3. A category column is added to the dataset
4. Spending totals are calculated per category

The rule-based approach keeps behaviour transparent, predictable, and easy to extend.

---

## How to Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py

