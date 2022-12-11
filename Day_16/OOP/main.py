from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, text_logo
import os


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
print(menu.get_items())

# prints welcome arts
print(logo, text_logo)

def main():    
    # take an order, return coffee object
    coffee = order_drink()
    # check if resources are enough to make coffee
    if not coffee_maker.is_resource_sufficient(coffee):
        main()
        return 0
    # take coins and make coffee 
    if money_machine.make_payment(coffee.cost):
        coffee_maker.make_coffee(coffee)
        main()
        return 0
    else:
        main()
        return 0

    



# check user order
def order_drink():
    coffee = input(f"What would you like to drink? ({menu.get_items().strip('/')}): ")
    # show resources of the machine
    if coffee == 'report':
        coffee_maker.report()
        money_machine.report()
        return order_drink()
    # turn off 
    elif coffee == "off":
        quit("Good Bye my Friend!")
    # return the ordered coffee
    elif menu.find_drink(coffee):
        return menu.find_drink(coffee)
    # ask again
    else:
        return order_drink()
        


main()