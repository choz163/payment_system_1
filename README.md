## Проект: Каталог продуктов


## Описание
Данный проект представляет собой каталог продуктов.
Каталог содержит категории и товары, которые хранятся в объектах классов Category и Product.

## Классы
Product: Представляет собой товар с такими атрибутами, как название, описание, цена и количество.

Category: Представляет собой категорию с такими атрибутами, как название, описание и список товаров.

## Функции
load_data_from_json(file_path): Загружает данные о категориях и товарах из файла JSON.

## Зависимости
Для работы проекта необходимы следующие библиотеки:

json: встроенная библиотека для работы с JSON.

## Использование
python = "^3.12"
flake8 = "^7.1.1"
mypy = "^1.13.0"
black = "^24.10.0"
isort = "^5.13.2"

Создайте объекты Product и Category с соответствующими данными.

Используйте методы и атрибуты классов для управления и доступа к данным о продуктах и категориях.

При необходимости загрузите данные из файла JSON с помощью функции load_data_from_json().

Пример использования

from src.catalog import Product, Category

# Создаем объекты Product
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Создаем объекты Category
category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])

# Печатаем информацию о категориях и товарах
print(category1.name)
print(category1.description)
for product in Проект: Каталог продуктов

Описание

Данный проект представляет собой каталог продуктов.
Каталог содержит категории и товары, которые хранятся в объектах классов Category и Product.


Классы

Product: Представляет собой товар с такими атрибутами, как название, описание, цена и количество.


Category: Представляет собой категорию с такими атрибутами, как название, описание и список товаров.


Smartphone: Подкласс Product, представляющий смартфоны с дополнительными атрибутами, такими как эффективность, модель, память и цвет.


LawnGrass: Подкласс Product, представляющий газонную траву с дополнительными атрибутами, такими как страна происхождения, период прорастания и цвет.


Функции

load_data_from_json(file_path): Загружает данные о категориях и товарах из файла JSON.


Зависимости

Для работы проекта необходимы следующие библиотеки:



json: встроенная библиотека для работы с JSON.


Использование

python = "^3.12"
flake8 = "^7.1.1"
mypy = "^1.13.0"
black = "^24.10.0"
isort = "^5.13.2"
Копировать

Создайте объекты Product, Category, Smartphone и LawnGrass с соответствующими данными.


Используйте методы и атрибуты классов для управления и доступа к данным о продуктах и категориях.


При необходимости загрузите данные из файла JSON с помощью функции load_data_from_json().


Пример использования


from src.catalog import Product, Category, Smartphone, LawnGrass

# Создаем объекты Product
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Создаем объекты Category
category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])

# Создаем объекты Smartphone
smartphone1 = Smartphone(
    "Samsung Galaxy S23 Ultra",
    "256GB, Серый цвет, 200MP камера",
    180000.0,
    5,
    95.5,
    "S23 Ultra",
    256,
    "Серый",
)
smartphone2 = Smartphone(
    "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
)
smartphone3 = Smartphone(
    "Xiaomi Redmi Note 11",
    "1024GB, Синий",
    31000.0,
    14,
    90.3,
    "Note 11",
    1024,
    "Синий",
)

# Создаем объекты LawnGrass
grass1 = LawnGrass(
    "Газонная трава",
    "Элитная трава для газона",
    500.0,
    20,
    "Россия",
    "7 дней",
    "Зеленый",
)
grass2 = LawnGrass(
    "Газонная трава 2",
    "Выносливая трава",
    450.0,
    15,
    "США",
    "5 дней",
    "Темно-зеленый",
)

# Печатаем информацию о категориях, товарах, смартфонах и траве
print(category1.name)
print(category1.description)
for product in category1.products:
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

print(category2.name)
print(category2.description)
for product in category2.products:
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

print(smartphone1.name)
print(smartphone1.description)
print(smartphone1.price)
print(smartphone1.quantity)
print(smartphone1.efficiency)
print(smartphone1.model)
print(smartphone1.memory)
print(smartphone1.color)

print(smartphone2.name)
print(smartphone2.description)
print(smartphone2.price)
print(smartphone2.quantity)
print(smartphone2.efficiency)
print(smartphone2.model)
print(smartphone2.memory)
print(smartphone2.color)

print(smartphone3.name)
print(smartphone3.description)
print(smartphone3.price)
print(smartphone3.quantity)
print(smartphone3.efficiency)
print(smartphone3.model)
print(smartphone3.memory)
print(smartphone3.color)

print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)

print(grass2.name)
print(grass2.description)
print(grass2.price)
print(grass2.quantity)
print(grass2.country)
print(grass2.germination_period)
print(grass2.color)

# Сложение товаров и категорий
smartphone_sum = smartphone1 + smartphone2
print(smartphone_sum)

grass_sum = grass1 + grass2
print(grass_sum)

try:
    invalid_sum = smartphone1 + grass1
except TypeError:
    print("Возникла ошибка TypeError при попытке сложения")
else:
    print("Не возникла ошибка TypeError при попытке сложения")

# Добавление продукта в категорию
category_smartphones = Category(
    "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
)
category_grass = Category(
    "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
)

category_smartphones.add_product(smartphone3)

print(category_smartphones.products)

print(Category.product_count)

try:
    category_smartphones.add_product("Not a product")
except TypeError:
    print("Возникла ошибка TypeError при добавлении не продукта")
else:
    print("Не возникла ошибка TypeError при добавлении не продукта").products:
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

print(category2.name)
print(category2.description)
for product in category2.products:
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)