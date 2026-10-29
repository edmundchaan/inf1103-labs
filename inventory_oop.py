import json
import os

from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


def load_inventory():
    inventory = Inventory()

    if os.path.exists(FILENAME):
        print("inventory.json found.")
        with open(FILENAME, "r") as file:
            text = file.read()
        if text.strip() != "":
            for item in json.loads(text):
                product = Product(item["id"], item["name"], item["price"], item["stock"])
                inventory.add_product(product)
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with an empty inventory.")

    return inventory


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
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


print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)

inventory = load_inventory()
show_menu()

while True:
    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        print("Add New Product")
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = get_valid_price("Price: ")
        stock = get_valid_stock("Stock Quantity: ")
        product = Product(product_id, name, price, stock)
        if inventory.add_product(product):
            print("Product added successfully!")
        else:
            print("A product with that ID already exists.")

    elif option == "3":
        print("Update Stock")
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)
        if product is None:
            print("Product not found.")
        else:
            print("Product Found:")
            print("Name:", product.get_name())
            print("Current Stock:", product.get_stock())
            new_stock = get_valid_stock("New Stock Quantity: ")
            inventory.update_stock(product_id, new_stock)
            print("Stock updated successfully!")

    elif option == "4":
        print("Search Product")
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)
        if product is None:
            print("Product not found.")
        else:
            print("Product Found")
            print("-" * 48)
            print("ID:", product.get_product_id())
            print("Name:", product.get_name())
            print(f"Price: ${product.get_price():.2f}")
            print("Stock:", product.get_stock())
            print("-" * 48)

    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 6.")
