"""Category entity of the e-commerce core."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.product import Product


class Category:
    """Категория товаров интернет-магазина."""

    name: str
    description: str
    products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализировать категорию и обновить общие счётчики."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
