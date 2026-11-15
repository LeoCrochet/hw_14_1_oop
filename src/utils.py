"""Утилиты для загрузки категорий и товаров из JSON-файла."""

import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product


def create_objects_from_json(path: str | Path) -> list[Category]:
    """Создать объекты Category и Product из JSON-файла."""
    with open(path, encoding="utf-8") as file:
        raw_data: list[dict[str, Any]] = json.load(file)

    categories: list[Category] = []
    for category_data in raw_data:
        products = [
            Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            for product_data in category_data["products"]
        ]
        categories.append(
            Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
        )
    return categories
