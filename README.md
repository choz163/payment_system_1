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


from src.catalog import Category, Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
