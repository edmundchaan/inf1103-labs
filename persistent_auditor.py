def get_valid_input():
     user_input = input("Enter stock quantity (or 'quit' to exit): ")
     if user_input == "quit":
         return "quit"
     if not (user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit())):
         print("Invalid input. Please enter a valid number.")
         return None

     quantity = int(user_input)

     if quantity < 0:
         print("Invalid input. Please enter a non-negative number.")
         return None

     return quantity

def process_delivery(current_total, new_value):
     return current_total + new_value

def calculate_tax(amount):
     return amount * 0.1

def generate_report(total_units, failed_attempts):
        print("Total delivieries processed: ", total_units)
        print("Number of failed/rejected entries:", failed_attempts)

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:     
        return 0, []

    if not lines:
        return 0, []

    total = int(lines[0])
    history = []
    for line in lines[1:]:
        history.append(int(line))

    return total, history

def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total) + "\n")
        for amount in history:
            file.write(str(amount) + "\n")
    print("Inventory saved to inventory.txt")   


inventory, history = load_inventory()
failed_attempts = 0
delivery_processed = 0

while True:

    result = get_valid_input()
    if result == "quit":
        save_inventory(inventory, history)
        break

    if result is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, result)
    history.append(result)
    delivery_processed += 1
    tax = calculate_tax(result)

    print("Delivery accepted: ", result, "| Tax: ", tax, "| Current inventory: ", inventory)


generate_report(delivery_processed, failed_attempts)
print("Inventory audit session ended.")