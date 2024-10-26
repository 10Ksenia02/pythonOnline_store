import json
import os
from config import DATA_DIR
from src.product import Product
from src.category import Category

products_path = os.path.join(DATA_DIR, "products.json")


def read_json(path: str) -> dict:
    """Читаем данные из JSON файла"""
    with open(products_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Выгрузка данных по категориям из JSON файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == '__main__':
    raw_data = read_json(products_path)
    # print(raw_data)
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)