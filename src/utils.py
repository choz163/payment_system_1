import json

from src.catalog import Category, Product


def load_data_from_json(file_path):
    """Функция для загрузки данных о категориях и товарах из файла JSON."""

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        category_name = category_data["name"]
        category_description = category_data["description"]
        products = []
        for product_data in category_data["products"]:
            product_name = product_data["name"]
            product_description = product_data["description"]
            product_price = product_data["price"]
            product_quantity = product_data["quantity"]
            product = Product(
                product_name, product_description, product_price, product_quantity
            )
            products.append(product)
        category = Category(category_name, category_description, products)
        categories.append(category)

    return categories