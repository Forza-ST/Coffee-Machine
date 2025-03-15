# Initialize Resources
water = 300
milk = 200
coffee = 100
money = 0.0

# Define menu with drink requirements and costs
menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
    }
}

machine_status = True

def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# Check Resources
def check_resources(drink):
    if water < menu[drink]["water"]:
        print("Sorry, not enough water.")
        return False
    elif milk < menu[drink]["milk"]:
        print("Sorry, not enough milk.")
        return False
    elif coffee < menu[drink]["coffee"]:
        print("Sorry, not enough coffee.")
        return False
    return True

def coffee_machine():
    global water, milk, coffee, money, machine_status
    
    while machine_status:
        user_input = input("What would you like? 'latte', 'cappuccino', 'espresso': ")

        if user_input == "off":
            machine_status = False
            print("Coffee machine is turned off")
            return

        if user_input == "report":
            report()
            continue

        # Check Valid Choice
        if user_input in menu:
            if check_resources(user_input):
                print(f"You chose {user_input}")
                # Process payment and make coffee would go here
                
                # Deduct resources
                water -= menu[user_input]["water"]
                milk -= menu[user_input]["milk"]
                coffee -= menu[user_input]["coffee"]
                money += menu[user_input]["cost"]
                
                print(f"Here is your {user_input}. Enjoy!")
            continue

        # This part is redundant but kept as per request
        if user_input == "espresso":
            print(f"You chose Espresso")
        elif user_input == "latte":
            print(f"You chose Latte")
        elif user_input == "cappuccino":
            print(f"You chose Cappuccino")
        else:
            print("Invalid input")

coffee_machine()
