import pytest

from src.catalog import Category, Product


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category1(product1, product2):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )


def test_create_product():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_set_price():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product.price = 800
    assert product.price == 800


def test_set_invalid_price():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    with pytest.raises(ValueError):
        product.price = -100


def test_new_product():
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_create_category():
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category._products == []


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_product_add(category1, product2):
    category1.add_product(product2)
    assert len(category1._products) == 3


def test_category_add(category1, product2):
    category2 = Category(
        "Ноутбуки",
        "Ноутбуки, как средство не только для работы, но и для развлечений",
        [product2],
    )
    category1.add_product(category2)
    assert len(category1._products) == 3


def test_product_add_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(
            Product.new_product(
                {
                    "product_name": "Не продукт",
                    "product_description": "",
                    "product_price": 0,
                    "product_quantity": 0,
                }
            )
        )
