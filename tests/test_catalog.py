import pytest

from src.catalog import BaseProduct, Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def lawn_grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def category1(product1, smartphone1, lawn_grass1):
    return Category(
        "Смартфоны и трава",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, smartphone1, lawn_grass1],
    )


def test_create_base_product():
    with pytest.raises(TypeError):
        BaseProduct(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )


def test_create_product():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_create_smartphone():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_create_lawn_grass():
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_set_price():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product.price = 800
    assert product.price == 800


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
        "Смартфоны и трава",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    assert category.name == "Смартфоны и трава"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category._products == []


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_smartphone_str(smartphone1):
    assert str(smartphone1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_lawn_grass_str(lawn_grass1):
    assert str(lawn_grass1) == "Газонная трава, 500.0 руб. Остаток: 20 шт."


def test_category_str(category1):
    assert str(category1) == "Смартфоны и трава, количество продуктов: 30 шт."


def test_product_add(category1, product1):
    category1.add_product(product1)
    assert len(category1._products) == 4


def test_smartphone_add(category1, smartphone1):
    category1.add_product(smartphone1)
    assert len(category1._products) == 4


def test_lawn_grass_add(category1, lawn_grass1):
    category1.add_product(lawn_grass1)
    assert len(category1._products) == 4


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


def test_smartphone_add_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(
            Smartphone.new_product(
                {
                    "product_name": "Не смартфон",
                    "product_description": "",
                    "product_price": 0,
                    "product_quantity": 0,
                    "product_efficiency": 0,
                    "product_model": "",
                    "product_memory": 0,
                    "product_color": "",
                }
            )
        )


def test_lawn_grass_add_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(
            LawnGrass.new_product(
                {
                    "product_name": "Не трава",
                    "product_description": "",
                    "product_price": 0,
                    "product_quantity": 0,
                    "product_country": "",
                    "product_germination_period": "",
                    "product_color": "",
                }
            )
        )
