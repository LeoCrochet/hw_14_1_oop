# HW 14.1 — OOP: E-commerce core

Домашнее задание по ООП (SkyPro). Ядро интернет-магазина на классах `Product` и `Category`:
описание товаров и категорий, автоматический подсчёт количества категорий и товаров.

## Функционал

- Класс `Product` — товар: название, описание, цена, количество в наличии.
- Класс `Category` — категория: название, описание, список товаров.
- Атрибуты класса `Category.category_count` и `Category.product_count` —
  автоматически обновляются при создании каждого нового объекта.
- Загрузка категорий и товаров из JSON-файла (`data/products.json`).
- Тесты на `pytest` с покрытием функционального кода (отчёт в `htmlcov/`).

## Структура проекта

```
src/product.py    — класс Product
src/category.py   — класс Category и счётчики классов
src/utils.py      — загрузка объектов из JSON
data/products.json — пример данных: 2 категории, 4 товара
main.py           — демонстрационный запуск
tests/            — тесты pytest (conftest с общими фикстурами)
htmlcov/          — HTML-отчёт покрытия тестами
```

## Требования

- Python 3.14+
- Poetry 2.x

## Установка

```bash
poetry install
```

## Запуск

```bash
poetry run python main.py
```

## Загрузка данных из JSON

Функция `create_objects_from_json` читает JSON-файл и возвращает список
готовых объектов `Category`, внутри которых лежат объекты `Product`:

```python
from src.utils import create_objects_from_json

categories = create_objects_from_json("data/products.json")

for category in categories:
    print(category.name, len(category.products))
```

Формат файла — список категорий, у каждой поле `products` со списком товаров:

```json
[
  {
    "name": "Смартфоны",
    "description": "Мобильные устройства",
    "products": [
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }
    ]
  }
]
```

## Тесты и покрытие

```bash
poetry run pytest --cov=src --cov-report=html -v
```

HTML-отчёт покрытия: `htmlcov/index.html`.

## Линтеры и форматирование

```bash
poetry run isort .
poetry run black .
poetry run flake8 .
poetry run mypy src tests main.py
```
