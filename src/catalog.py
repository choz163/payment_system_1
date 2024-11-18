class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    count_categories = 0
    count_products = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products
        Category.count_categories += 1
        Category.count_products += len(self._products)

    @property
    def products(self):
        products_str = ""
        for product in self._products:
            products_str += f"{product}\n"
        return products_str

    def add_product(self, product):
        self._products.append(product)
        Category.count_products += 1

    def __str__(self):
        total_quantity = 0
        for product in self._products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __add__(self, other):
        return sum(
            product.price * product.quantity for product in self._products
        ) + sum(product.price * product.quantity for product in other._products)
