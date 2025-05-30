water = 300,
milk = 200,
coffee = 100,
money = 0.0

def menu = {
    proprotions = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
    }

}

machine_status = True

while machine_status == "on":





}

IF choice is a valid drink (espresso, latte, or cappuccino):
            CHECK if enough resources for the drink:
                IF any resource (water, milk, coffee) is insufficient:
                    INFORM user which resource is lacking
                    RETURN to main prompt

def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# Check Resources

def check_resources(drink):
    if amount(resources, drink):





def coffee_machine():
    while machine_status:
        user_input = input("What would you like? 'latte', 'cappuccino', 'espresso': ")

        if user_input == "off":
            machine_status = False

        # Print Report


        if user_input == "espresso":
            print(f"You chose Espresso")
            
        elif user_input == "latte":
            print(f"You chose Latte")
        elif user_input == "cappuccino":
            print(f"You chose Cappuccino")
        elif user_input == "off":
            print("Coffee machine is turned off")
        else:
            print("Invalid input")

coffee_machine()

# Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

## 2. Turn off the Coffee Machine
# - Turn off the Coffee Machine by entering "off" to the prompt.
#   - For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine. Your code should end execution when this happens.

## 3. Print Report
''' When the user enters "report" to the prompt, a report should be generated that shows the current resource values. e.g.
  
  Water: 100ml
  Milk: 50ml
  Coffee: 76g
  Money: $2.5
  '''

## 4. Check Resources
# - When the user chooses a drink, the program should check if there are enough resources to make that drink.
#   - E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: "Sorry there is not enough water."
#   - The same should happen if another resource is depleted, e.g. milk or coffee.

## 5. Process Coins
# - If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#   - Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#   - Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

## 6. Check Transaction
# - Check that the user has inserted enough money to purchase the drink they selected.
#   - E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say "Sorry that's not enough money. Money refunded."
#   - But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered. E.g.
#     ```
#     Water: 100ml
#     Milk: 50ml
#     Coffee: 76g
#     Money: $2.5
#     ```
#   - If the user has inserted too much money, the machine should offer change. E.g. "Here is $2.45 dollars in change." The change should be rounded to 2 decimal places.

## 7. Make Coffee
# - If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
#   - E.g. report before purchasing latte:
#     ```
#     Water: 300ml
#     Milk: 200ml
#     Coffee: 100g
#     Money: $0
#     ```
#   - Report after purchasing latte:
#     ```
#     Water: 100ml
#     Milk: 50ml
#     Coffee: 76g
#     Money: $2.5
#     ```
#   - Once all resources have been deducted, tell the user "Here is your latte. Enjoy!". If latte was their choice of drink.


