# Smart Inventory Auditor
# Initializes inventory at zero and keeps accepting integer quantities until the user quits.

inventory = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ")

    if user_input.strip().lower() == "quit":
        break

    try:
        quantity = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number or 'quit'.")
        continue

    if quantity < 0:
        print("Negative values are not allowed. Please enter a non-negative integer.")
        continue

    inventory += quantity
    print(f"Current inventory: {inventory}")

print("Inventory audit session ended.")
