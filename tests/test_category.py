"""Тесты класса Category."""

from src.category import Category
from src.product import Product


def test_category_init_sets_all_fields(product_one: Product, product_two: Product) -> None:
    """Проверить, что название, описание и список товаров сохранены."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны для повседневного использования",
        products=[product_one, product_two],
    )

    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для повседневного использования"
    assert isinstance(category.products, list)
    assert len(category.products) == 2
    assert category.products == [product_one, product_two]


def test_category_products_contain_product_instances(product_one: Product) -> None:
    """В списке товаров должны лежать именно объекты Product."""
    category = Category(name="Смартфоны", description="Описание", products=[product_one])

    assert all(isinstance(item, Product) for item in category.products)


def test_category_with_empty_product_list() -> None:
    """Пустая категория допустима и не увеличивает product_count."""
    category = Category(name="Пустая", description="Пока без товаров", products=[])

    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_count_after_one_category(product_one: Product, product_two: Product) -> None:
    """После создания одной категории category_count равен 1, product_count — числу товаров."""
    Category(name="Смартфоны", description="Описание", products=[product_one, product_two])

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_count_after_two_categories(product_one: Product, product_two: Product) -> None:
    """Счётчики складываются по всем созданным категориям и товарам."""
    first = Category(name="Смартфоны", description="Описание", products=[product_one, product_two])
    Category(name="Телевизоры", description="Описание", products=[product_one])

    assert Category.category_count == 2
    assert Category.product_count == 3
    assert first.category_count == 2
    assert first.product_count == 3
