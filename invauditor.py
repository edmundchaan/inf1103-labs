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