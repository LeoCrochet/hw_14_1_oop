"""Тесты класса Product."""

import pytest

from src.product import Product


def test_product_init_sets_all_fields(product_one: Product) -> None:
    """Проверить, что все четыре поля сохранены при инициализации."""
    assert product_one.name == "Samsung Galaxy S23 Ultra"
    assert product_one.description == "256GB, Серый цвет, 200MP камера"
    assert product_one.price == 180000.0
    assert product_one.quantity == 5


def test_product_field_types(product_one: Product) -> None:
    """Цена должна быть float, количество — int."""
    assert isinstance(product_one.name, str)
    assert isinstance(product_one.description, str)
    assert isinstance(product_one.price, float)
    assert isinstance(product_one.quantity, int)


@pytest.mark.parametrize(
    ("name", "description", "price", "quantity"),
    [
        ("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ],
)
def test_product_init_with_different_values(
    name: str,
    description: str,
    price: float,
    quantity: int,
) -> None:
    """Инициализация корректно работает с разными наборами данных."""
    product = Product(name=name, description=description, price=price, quantity=quantity)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


def test_product_init_with_zero_values() -> None:
    """Граничный случай: нулевая цена и нулевое количество допустимы."""
    product = Product(name="Пустышка", description="Нет в наличии", price=0.0, quantity=0)

    assert product.price == 0.0
    assert product.quantity == 0
