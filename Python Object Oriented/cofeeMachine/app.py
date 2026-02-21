class ResourceError(Exception):
    """Custom exception for resource-related errors."""
    pass

class PaymentError(Exception):
    """Custom exception for payment-related errors."""
    pass

class Resources:
    """Manages the ingredients available in the coffee machine."""
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def get_report(self):
        """Returns a formatted string of current resource levels."""
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g"

    def check_sufficient(self, drink):
        """Checks if there are enough resources to make a drink. Raises ResourceError if not."""
        for ingredient, amount in drink.ingredients.items():
            if getattr(self, ingredient) < amount:
                raise ResourceError(f"Sorry, there is not enough {ingredient}.")
        return True

    def deduct(self, drink):
        """Deducts the required ingredients for a drink from inventory."""
        for ingredient, amount in drink.ingredients.items():
            setattr(self, ingredient, getattr(self, ingredient) - amount)

class MoneyHandler:
    """Manages all monetary transactions, including coin processing and profit."""
    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

    def __init__(self):
        self.profit = 0.0

    def get_report(self):
        """Returns a formatted string of the current profit."""
        return f"Money: ${self.profit:.2f}"

    def process_payment(self, cost):
        """Processes coins from the user and returns change if successful. Raises PaymentError on failure."""
        print("Please insert coins.")
        total_inserted = 0
        for coin, value in self.COIN_VALUES.items():
            try:
                num_coins = int(input(f"How many {coin}?: "))
                total_inserted += num_coins * value
            except ValueError:
                print("Invalid input. Please enter a whole number for coins.")
        
        if total_inserted < cost:
            raise PaymentError(f"Sorry, that's not enough money. ${total_inserted:.2f} refunded.")
        
        change = round(total_inserted - cost, 2)
        self.profit += cost
        print(f"Here is ${change:.2f} in change.")
        return True

class CoffeeDrink:
    """A base class for a coffee drink, defining its core attributes."""
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

class Espresso(CoffeeDrink):
    """An Espresso drink, inheriting from CoffeeDrink."""
    def __init__(self):
        super().__init__("espresso", 1.5, {"water": 50, "coffee": 18, "milk": 0})

class Latte(CoffeeDrink):
    """A Latte drink, inheriting from CoffeeDrink."""
    def __init__(self):
        super().__init__("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24})

class Cappuccino(CoffeeDrink):
    """A Cappuccino drink, inheriting from CoffeeDrink."""
    def __init__(self):
        super().__init__("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})

class CoffeeMachine:
    """The main class that orchestrates the coffee making process."""
    def __init__(self):
        self.resources = Resources(water=500, milk=400, coffee=200)
        self.money_handler = MoneyHandler()
        self.menu = {
            "espresso": Espresso(),
            "latte": Latte(),
            "cappuccino": Cappuccino()
        }

    def report(self):
        """Prints a report of all resources and money."""
        print("\n--- Machine Report ---")
        print(self.resources.get_report())
        print(self.money_handler.get_report())
        print("----------------------\n")

    def make_drink(self, choice):
        """Handles the entire process of making a coffee."""
        drink = self.menu.get(choice)
        if not drink:
            print("Invalid selection. Please try again.")
            return

        try:
            self.resources.check_sufficient(drink)
            self.money_handler.process_payment(drink.cost)
            self.resources.deduct(drink)
            print(f"Here is your {drink.name} ☕. Enjoy!")
        except (ResourceError, PaymentError) as e:
            print(e) # Print the specific error message from the exception

    def run(self):
        """Starts the coffee machine and prompts the user for input."""
        is_on = True
        while is_on:
            menu_items = "/".join(self.menu.keys())
            choice = input(f"What would you like? ({menu_items}/report/off): ").lower()
            if choice == "off":
                is_on = False
                print("Turning off the machine.")
            elif choice == "report":
                self.report()
            else:
                self.make_drink(choice)

if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()