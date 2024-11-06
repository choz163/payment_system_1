

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    count_categories = 0
    count_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.count_categories += 1
        Category.count_products += len(self.products)