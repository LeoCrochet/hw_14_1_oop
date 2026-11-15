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
