"""Product entity of the e-commerce core."""


class Product:
    """Товар интернет-магазина."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализировать товар с заданными характеристиками."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
