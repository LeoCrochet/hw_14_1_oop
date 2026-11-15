"""Общие фикстуры для тестов."""

from collections.abc import Iterator

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> Iterator[None]:
    """Сбрасывать счётчики Category, чтобы тесты не влияли друг на друга."""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def product_one() -> Product:
    """Готовый товар для тестов."""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_two() -> Product:
    """Второй товар для тестов."""
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )
