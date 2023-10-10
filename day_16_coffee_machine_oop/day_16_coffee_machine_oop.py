from main import CoffeeMaker, MoneyMachine, Menu, MenuItem

# initialize necessary objects
coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# get drink choice from user
select_drink = input(f"What would you like to drink: {menu.get_items()}\nEnter your selection: ").lower()
# assign drink variable to appropriate MenuItem
drink = menu.find_drink(select_drink)

# if machine has resources for drink, take payment and make drink, otherwise print error message
if coffee_machine.is_resource_sufficient(drink):
    print(f"{drink.name}: ${drink.cost}")
    money_machine.make_payment(drink.cost)
    coffee_machine.make_coffee(drink)
else:
    print("Insufficient resources to make beverage.")