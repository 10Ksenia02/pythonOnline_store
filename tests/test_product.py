from src.product import Product

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_samsung(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_iphone(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000


def test_new_str(product_str_1, product_str_2):
    assert product_str_1 == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert product_str_2 == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_counter(counter, counter_2, product_1, product_2, product_3):
    assert product_1 + product_2 == counter
    assert product_2 + product_3 == counter_2
