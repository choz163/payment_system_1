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