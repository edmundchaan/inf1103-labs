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
     


inventory = 0
failed_attempts = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ")

    if user_input == "quit":
        print("Total Units Processed:", inventory)
        print("Failed Attempts:", failed_attempts)
        break
    

    if not (user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit())):
        print("Invalid input. Please enter a valid number.")
        failed_attempts += 1
        continue

    if int(user_input) < 0:
        print("Invalid input. Please enter a non-negative number.")
        failed_attempts += 1
        continue

    quantity = int(user_input)
    inventory += quantity

    if inventory > 500:
            print("Warning: Inventory exceeds maximum capacity of 500 units.")
            break
    
    print("Current inventory:", inventory)

print("Inventory audit session ended.")