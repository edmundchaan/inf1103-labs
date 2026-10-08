import json
import os

FILENAME = "inventory.json"


def display_all(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    print("Current Inventory")
    print("-" * 48)
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 48)

def search_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def add_product(inventory, product_id, name, price, stock):
    if search_product(inventory, product_id) is not None:
        return False
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    return True

def update_stock(inventory, product_id, new_stock):
    product = search_product(inventory, product_id)
    if product is None:
        return False
    product["stock"] = new_stock
    return True

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.0, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.5, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.0, "stock": 25},
]
print(update_stock(inventory, "P002", 50))
print(update_stock(inventory, "P999", 5))
display_all(inventory)