'''program simulating a coffee machine'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

class CoffeeMachine:
    def __init__(self):
        self._menu = MENU.copy()
        self._resources = resources.copy()
        self.user_order = None # user's order to be assigned
        self.order_resources = None # ingredients of user's order to be checked against machine's available resources
        self.money_owed = None # amount needed for user's order
        self.money_deposited = None # amount user has entered
        self.artwork = '''
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'    
    '''

    # print report of resources
    def print_report(self):
        print("\nRESOURCES:")
        for key, value in self._resources.items():
            print(f"- {key.title()}: {value}")

    # print out menu options available
    def print_menu(self):
        print("\nMENU:")
        for key in self._menu:
            print("-", key.title())

    def order(self):
    # run order sequence: select coffee, check resources, take payment, and vend
        
        def select_beverage():
            # have user select a beverage, verify beverage is on the menu
            print("\n🤖 \"Drip drop, I'm a coffee robot...  What would you like to drink?\"")
            self.print_menu()

            _ = input("\nSelect an item from the list above: ").lower()
                
            if _ in self._menu.keys():
                self.user_order = _
            else:
                print("\n🤖 \"Wake up, Rip Van Winke. That item is not on the menu. Please try again.\"")
                select_beverage()


        def check_resources():
            # check if resources needed for order are available in machine
            self.order_resources = self._menu[self.user_order]['ingredients']
            resources_checked = 0
                    
            for resource, amount_needed in self.order_resources.items():
                if self._resources[resource] < amount_needed:
                    print(f"\nInsufficent {resource} for order: {self._resources[resource]}. Please add more {resource} and try again.")
                    break
                else:
                    resources_checked += 1
            if resources_checked == len(self.order_resources):
                return True
            else:
                return False
        
        
        def get_payment():
            # set balance owed from user, and have user enter coins to reduce balance owed
            self.money_owed = self._menu[self.user_order]['cost']
            self.money_deposited = 0
            coins = {"quarters" : 0.25, "dimes" : 0.1, "nickels" : 0.05, "pennies" : 0.01}

            print(f"🤖 \"Your total is: ${self.money_owed}0. Please insert payment now, sleepyhead.")

            while self.money_owed > self.money_deposited:
                for coin_name, coin_value in coins.items():
                    _ = int(input(f"\nInput how many {coin_name}?\nEnter a number: "))
                    self.money_deposited += (_ * coin_value)
                    self.money_owed -= (_ * coin_value)
                    print(f"\nDeposited: ${self.money_deposited}0\nRemaining balance: ${self.money_owed}0")
                    if self.money_owed <= 0:
                        break
                
            print(f"\nPayment received.\nChange: ${self.money_owed}0")
        

        def vend_beverage():
            # subtract resources needed for user's beverage from the machine resource totals, print funny vend sequence
            for resource in self._resources.keys():
                if resource in self.order_resources.keys():
                    self._resources[resource] -= self.order_resources[resource]

            input(f"\n🤖 \"Now brewing...\"")
            input(f"🤖 \"Please feel free to tap impatiently on your return key while you wait.\"")
            input("...")
            input(".....")
            input("........(What time is it??)...")
            input("🤖 \"Sorry, no speed upgrade available in coffee robot database.\"")
            input("...")
            input("...... 🔔 DING!")
            print(f"🤖 \"One {self.user_order}, hotter than you can handle. Enjoy!\"")
            print(self.artwork)
        
        # main order, resource-check, payment, and vend sequence
        select_beverage()

        if check_resources() == True:
            print(f"\nOrder for 1 {self.user_order} confirmed.")
            get_payment()
            vend_beverage()
        else:
            print(f"\nSorry, order not accepted. Please check machine resources and try again.\n"
            "\n🤖 \"MAINTENANNNNNCE!!! ⚡bzzzrtbpt⚡\"")

if __name__ == "__main__":
    coffee_robot = CoffeeMachine()
    coffee_robot.order() # repeat to order multiple coffees, or to see result of machine running out of resource(s)