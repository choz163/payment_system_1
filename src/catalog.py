from abc import ABC, abstractmethod
from typing import List


class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(
            f"Создан объект класса {self.__class__.__name__} с параметрами: name={name}, description={description}, price={price}, quantity={quantity}"
        )

    @abstractmethod
    def __str__(self):
        pass


class Product(BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект класса {self.__class__.__name__} с параметрами: {args}, {kwargs}"
        )


class Smartphone(Product, LogMixin):
    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        efficiency,
        model,
        memory,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class LawnGrass(Product, LogMixin):
    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        country,
        germination_period,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class Category:
    category_count = 0
    count_products = 0
    product_count = 0

    def __init__(self, name, description, products: List[Product]):
        self.name = name
        self.description = description
        self._products = products
        Category.category_count += 1
        Category.count_products += len(self._products)

    @property
    def products(self):
        products_str = ""
        for product in self._products:
            products_str += f"{product}\n"
        return products_str

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self._products.append(product)

    def __str__(self):
        total_quantity = 0
        for product in self._products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __add__(self, other):
        if isinstance(self, other.__class__):
            return sum(
                product.price * product.quantity for product in self._products
            ) + sum(product.price * product.quantity for product in other._products)
        else:
            raise TypeError("Можно складывать только объекты одного класса")

    def middle_price(self):
        try:
            return sum(
                product.price * product.quantity for product in self._products
            ) / len(self._products)
        except ZeroDivisionError:
            return 0
