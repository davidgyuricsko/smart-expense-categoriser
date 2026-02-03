from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class CategoryRule:
    category: str
    keywords: List[str]


DEFAULT_RULES: List[CategoryRule] = [
    CategoryRule("Food & Drink", ["starbucks", "pret", "deliveroo", "uber eats", "mcdonald", "kfc", "pizza"]),
    CategoryRule("Groceries", ["tesco", "aldi", "lidl", "sainsbury", "asda", "waitrose", "morrisons"]),
    CategoryRule("Transport", ["uber", "bolt", "national rail", "tfl", "train", "bus", "shell", "petrol", "bp", "esso"]),
    CategoryRule("Entertainment", ["netflix", "spotify", "cinema", "prime video", "disney"]),
    CategoryRule("Shopping", ["amazon", "ikea", "argos", "ebay"]),
    CategoryRule("Income", ["salary", "payroll"]),
]


def categorise_description(description: str, rules: List[CategoryRule] = DEFAULT_RULES) -> str:
    """
    Return a category name for a transaction description using simple keyword rules.
    """
    text = (description or "").lower().strip()

    if not text:
        return "Uncategorised"

    for rule in rules:
        for kw in rule.keywords:
            if kw in text:
                return rule.category

    return "Other"
