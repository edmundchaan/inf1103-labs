inventory = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ")

    if user_input == "quit":
        break
    

    if not (user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit())):
        print("Invalid input. Please enter a valid number.")
        continue

    if int(user_input) < 0:
        print("Invalid input. Please enter a non-negative number.")
        continue

    quantity = int(user_input)
    inventory = inventory + quantity
    print("Current inventory:", inventory)

print("Inventory audit session ended.")