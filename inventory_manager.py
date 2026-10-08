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

def load_inventory():
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        with open(FILENAME, "r") as file:
            text = file.read()
        if text.strip() == "":
            return []
        inventory = json.loads(text)
        print("Inventory loaded successfully.")
        return inventory

    print("inventory.json not found. Starting with an empty inventory.")
    return []


def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully to inventory.json.")

def get_valid_stock(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a whole number (0 or more).")


def get_valid_price(prompt):
    while True:
        value = input(prompt)
        if value.replace(".", "", 1).isdigit():
            return float(value)
        print("Invalid input. Please enter a valid price, e.g. 25.50.")


def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    
inventory = load_inventory()
display_all(inventory)