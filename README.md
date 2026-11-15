# HW 14.1 — OOP: E-commerce core

Домашнее задание по ООП (SkyPro). Ядро интернет-магазина на классах `Product` и `Category`:
описание товаров и категорий, автоматический подсчёт количества категорий и товаров.

## Функционал

- Класс `Product` — товар: название, описание, цена, количество в наличии.
- Класс `Category` — категория: название, описание, список товаров.
- Атрибуты класса `Category.category_count` и `Category.product_count` —
  автоматически обновляются при создании каждого нового объекта.
- Тесты на `pytest` с покрытием функционального кода (отчёт в `htmlcov/`).
- (доп.) Загрузка категорий и товаров из JSON-файла.

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