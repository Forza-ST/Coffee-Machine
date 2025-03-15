COFFEE MACHINE PROGRAM

INITIALIZE resources:
    Set water to 300ml
    Set milk to 200ml
    Set coffee to 100g
    Set money to $0.00

DEFINE menu with drink requirements:
    espresso requires 50ml water, 18g coffee, 0ml milk, costs $1.50
    latte requires 200ml water, 24g coffee, 150ml milk, costs $2.50
    cappuccino requires 250ml water, 24g coffee, 100ml milk, costs $3.00

SET machine status to ON

MAIN OPERATION:
    WHILE machine is ON:
        ASK user "What would you like? (espresso/latte/cappuccino):"
        STORE user's answer as choice
        
        IF choice is "off":
            SET machine status to OFF
            END program
        
        IF choice is "report":
            DISPLAY current resource levels:
                Water amount in ml
                Milk amount in ml
                Coffee amount in g
                Money amount in $
        
        IF choice is a valid drink (espresso, latte, or cappuccino):
            CHECK if enough resources for the drink:
                IF any resource (water, milk, coffee) is insufficient:
                    INFORM user which resource is lacking
                    RETURN to main prompt
                
                OTHERWISE:
                    PROMPT user to insert coins:
                        ASK for number of quarters ($0.25)
                        ASK for number of dimes ($0.10)
                        ASK for number of nickels ($0.05)
                        ASK for number of pennies ($0.01)
                    
                    CALCULATE total money inserted
                    
                    IF total money is less than drink cost:
                        INFORM user "Sorry that's not enough money. Money refunded."
                    
                    OTHERWISE:
                        IF total money exceeds drink cost:
                            CALCULATE change amount (total inserted minus drink cost)
                            RETURN change to user, rounded to 2 decimal places
                        
                        ADD drink cost to machine's money resource
                        
                        DEDUCT required resources from machine:
                            Subtract required water from available water
                            Subtract required milk from available milk
                            Subtract required coffee from available coffee
                        
                        SERVE the drink with message "Here is your [drink name]. Enjoy!"
        
        IF choice is invalid:
            INFORM user of invalid selection
            
    END WHILE
