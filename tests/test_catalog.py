import pytest

from src.catalog import Product, Category

def test_create_product():
    product = Product("Товар 1", "Описание товара 1", 100, 10)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100
    assert product.quantity == 10

def test_set_price():
    product = Product("Товар 1", "Описание товара 1", 100, 10)
    product.price = 200
    assert product.price == 200

def test_set_invalid_price():
    product = Product("Товар 1", "Описание товара 1", 100, 10)
    with pytest.raises(ValueError) as excinfo:
        product.price = -100
    assert "Цена не должна быть нулевая или отрицательная" in str(excinfo.value)


def test_new_product():
    product_data = {"name": "Товар 1", "description": "Описание товара 1", "price": 100, "quantity": 10}
    product = Product.new_product(product_data)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100
    assert product.quantity == 10


def test_create_category():
    category = Category("Категория 1", "Описание категории 1", [])
    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert category.products == ""
    assert Category.count_categories == 1
    assert Category.count_products == 0

def test_add_product():
    category = Category("Категория 1", "Описание категории 1", [])
    product = Product("Товар 1", "Описание товара 1", 100, 10)
    category.add_product(product)
    assert category.products == "Товар 1, 100 руб. Остаток: 10 шт.\n"
    assert Category.count_products == 1
