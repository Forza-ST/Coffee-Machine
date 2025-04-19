# Initialize Resources (Realistic amounts)
water = 2000      # in ml (2 liters)
milk = 1000       # in ml (1 liter)
coffee = 500      # in grams
money = 0.0

# Drink menu with emojis and realistic recipes
menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5,
        "emoji": "☕️"
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
        "emoji": "🥛☕️"
    },
    "cappuccino": {
        "water": 150,
        "milk": 120,
        "coffee": 24,
        "cost": 3.0,
        "emoji": "☕️✨"
    }
}

machine_status = True

# Print current resource report
def report():
    print(f"💧 Water: {water} ml")
    print(f"🥛 Milk: {milk} ml")
    print(f"☕️ Coffee: {coffee} g")
    print(f"💰 Money: ${money:.2f}")

# Check if resources are sufficient
def check_resources(drink):
    if water < menu[drink]["water"]:
        print("🚫 Sorry, not enough water.")
        return False
    if milk < menu[drink]["milk"]:
        print("🚫 Sorry, not enough milk.")
        return False
    if coffee < menu[drink]["coffee"]:
        print("🚫 Sorry, not enough coffee.")
        return False
    return True

# Calculate total inserted money
def calculate_total_money():
    quarters = int(input("How many quarters ($0.25)? "))
    dimes = int(input("How many dimes ($0.10)? "))
    nickels = int(input("How many nickels ($0.05)? "))
    pennies = int(input("How many pennies ($0.01)? "))
    total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_money

# Process payment
def process_payment(drink_cost):
    total_money = calculate_total_money()
    if total_money < drink_cost:
        print("🚫 Sorry that's not enough money. Money refunded.")
        return False
    elif total_money > drink_cost:
        change = round(total_money - drink_cost, 2)
        print(f"💵 Here is ${change:.2f} in change.")
    return True

# Main Coffee Machine Logic
def coffee_machine():
    global water, milk, coffee, money, machine_status

    while machine_status:
        user_input = input("\nWhat would you like? (espresso/latte/cappuccino/report/off/refill): ").lower()

        if user_input == "off":
            machine_status = False
            print("🛑 Coffee machine turning off...")
            break

        elif user_input == "report":
            report()

        elif user_input == "refill":
            water, milk, coffee = 2000, 1000, 500
            print("🔄 Machine refilled successfully!")

        elif user_input in menu:
            drink = menu[user_input]

            if check_resources(user_input):
                print(f"✅ You chose {user_input.title()} {drink['emoji']} (${drink['cost']:.2f}). Please insert coins.")
                if process_payment(drink["cost"]):
                    # Deduct resources and add money
                    water -= drink["water"]
                    milk -= drink["milk"]
                    coffee -= drink["coffee"]
                    money += drink["cost"]
                    print(f"🎉 Here is your {user_input.title()}! {drink['emoji']} Enjoy!")
        else:
            print("❗ Invalid choice. Please try again.")

coffee_machine()
