"""Общие фикстуры для тестов."""

import json
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any

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


@pytest.fixture
def json_writer() -> Callable[[Path, object], Path]:
    """Фабрика: записать данные в JSON-файл и вернуть путь к нему."""

    def _write_json(path: Path, data: object) -> Path:
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return path

    return _write_json


@pytest.fixture
def products_json_data() -> list[dict[str, Any]]:
    """Данные двух категорий: 2 товара + 1 товар."""
    return [
        {
            "name": "Смартфоны",
            "description": "Мобильные устройства",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "ТВ-техника",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]


@pytest.fixture
def products_json_path(
    tmp_path: Path,
    json_writer: Callable[[Path, object], Path],
    products_json_data: list[dict[str, Any]],
) -> Path:
    """Путь к временному JSON-файлу с товарами и категориями."""
    return json_writer(tmp_path / "products.json", products_json_data)


@pytest.fixture
def empty_json_path(
    tmp_path: Path,
    json_writer: Callable[[Path, object], Path],
) -> Path:
    """Путь к временному JSON-файлу с пустым списком."""
    return json_writer(tmp_path / "empty.json", [])
