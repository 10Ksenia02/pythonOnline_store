from src.category import Category
from src.product import Product

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_category_tv(category_tv, product_4):
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                                       " станет вашим другом и помощником")
    assert category_tv.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'


def test_category_smart(category_smart, product_1, product_2, product_3):
    assert category_smart.name == "Смартфоны"
    assert category_smart.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert category_smart.products == '''Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'''



def test_category(category_smart, product_4):
    was_products = Category.product_count
    category_smart.add_product(product_4)
    category_smart.add_product(new_product)
    assert Category.product_count == was_products + 2
