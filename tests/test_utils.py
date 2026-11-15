"""Тесты загрузки категорий и товаров из JSON."""

from pathlib import Path

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json


def test_create_objects_from_json_returns_categories(products_json_path: Path) -> None:
    """Функция создаёт объекты Category с объектами Product внутри."""
    categories = create_objects_from_json(products_json_path)

    assert len(categories) == 2
    assert all(isinstance(category, Category) for category in categories)

    first = categories[0]
    assert first.name == "Смартфоны"
    assert first.description == "Мобильные устройства"
    assert len(first.products) == 2
    assert all(isinstance(product, Product) for product in first.products)

    product = first.products[0]
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_create_objects_from_json_updates_counters(products_json_path: Path) -> None:
    """Счётчики Category заполняются по данным из JSON."""
    create_objects_from_json(products_json_path)

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_create_objects_from_json_with_empty_list(empty_json_path: Path) -> None:
    """Пустой JSON даёт пустой список категорий."""
    assert create_objects_from_json(empty_json_path) == []


def test_create_objects_from_json_reads_project_file() -> None:
    """Реальный data/products.json из репозитория загружается корректно."""
    categories = create_objects_from_json(Path("data") / "products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1
