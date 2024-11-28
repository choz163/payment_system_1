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
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
        )

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )

    try:
        print(category1.middle_price())
    except ZeroDivisionError:
        print("В категории нет товаров")
    else:
        print("Средний ценник в категории:", category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
