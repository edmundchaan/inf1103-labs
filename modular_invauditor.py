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

     


inventory = 0
failed_attempts = 0
delivery_processed = 0

while True:

    result = get_valid_input()
    if result == "quit":
        break

    if result is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, result)
    delivery_processed += 1
    tax = calculate_tax(result)

    print("Delivery accepted: ", result, "| Tax: ", tax, "| Current inventory: ", inventory)


generate_report(inventory, failed_attempts)
print("Inventory audit session ended.")