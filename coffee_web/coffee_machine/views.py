from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CoffeeMachine

resources = {'water': 2000, 'milk': 1000, 'coffee': 500, 'money': 0.0}

menu = {
    'espresso': {'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.5},
    'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
    'cappuccino': {'water': 150, 'milk': 120, 'coffee': 24, 'cost': 3.0}
}

def home(request):
    return render(request, 'coffee_machine/home.html', {'menu': menu})

def order(request, drink_name):
    return render(request, 'coffee_machine/order.html', {
        'drink_name': drink_name,
        'drink_info': menu[drink_name]
    })


def make_coffee(request):
    drink_type = request.POST.get('drink_type')
    
    if not drink_type or drink_type not in menu:
        messages.error(request, "Sorry, that drink is not available.")
        return redirect('home')
    
    drink = menu[drink_type]

    # Get the CoffeeMachine instance (assuming only one coffee machine in the system)
    coffee_machine = CoffeeMachine.objects.first()  # You could use `.first()` or `.get(id=1)` for a specific machine
    
    if coffee_machine is None:
        messages.error(request, "Coffee machine not found.")
        return redirect('home')

    # Check if resources are available in the CoffeeMachine model
    missing_item = check_resources(drink, coffee_machine)
    if missing_item:
        messages.error(request, f"Sorry, not enough {missing_item}.")
        return redirect('home')

    # Deduct ingredients from the CoffeeMachine instance
    for item in ['water', 'milk', 'coffee']:
        setattr(coffee_machine, item, getattr(coffee_machine, item) - drink[item])
    
    # Add money to the coffee machine
    coffee_machine.money += drink['cost']
    
    # Save the updated CoffeeMachine instance
    coffee_machine.save()

    # Display a success message
    messages.success(request, f"Here's your {drink_type.title()} ☕️ Enjoy!")
    return redirect('home')





def make_coffee(request):
    drink = menu[request.POST['drink_type']]
    for item in ['water', 'milk', 'coffee']:
        if resources[item] < drink[item]:
            messages.error(request, f"Sorry, not enough {item}.")
            return redirect('home')
        resources[item] -= drink[item]
    resources['money'] += drink['cost']
    messages.success(request, f"Here's your {request.POST['drink_type'].title()} ☕️ Enjoy!")
    return redirect('home')

def refill(request):
    resources.update({'water': 2000, 'milk': 1000, 'coffee': 500})
    messages.success(request, "Resources refilled! ✅")
    return redirect('home')

def report(request):
    return render(request, 'coffee_machine/report.html', {'resources': resources})
