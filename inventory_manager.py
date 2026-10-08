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
    
print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)

inventory = load_inventory()
show_menu()

while True:
    option = input("Enter option: ")

    if option == "1":
        display_all(inventory)

    elif option == "2":
        print("Add New Product")
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = get_valid_price("Price: ")
        stock = get_valid_stock("Stock Quantity: ")
        if add_product(inventory, product_id, name, price, stock):
            print("Product added successfully!")
        else:
            print("A product with that ID already exists.")

    elif option == "3":
        print("Update Stock")
        product_id = input("Enter Product ID: ")
        product = search_product(inventory, product_id)
        if product is None:
            print("Product not found.")
        else:
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])
            new_stock = get_valid_stock("New Stock Quantity: ")
            update_stock(inventory, product_id, new_stock)
            print("Stock updated successfully!")

    elif option == "4":
        print("Search Product")
        product_id = input("Enter Product ID: ")
        product = search_product(inventory, product_id)
        if product is None:
            print("Product not found.")
        else:
            print("Product Found")
            print("-" * 48)
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
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