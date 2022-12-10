from art import logo, text_logo
from database import MENU, resources
from sys import exit



def main(actual_resources=resources, menu=MENU, introduction=True):
    """ resources argument is a dictionary of resources in the maachine, menu is list of coffee dictionaries with all ingredients that are needed for the coffee """
    if introduction:
        print(logo)
        print(text_logo)
    # ask user which coffee he wants and check if machine have enough ingredients for that coffee
    # also ask user to insert coins and check if it is enough
    coffee, cost, coffee_ingredients = ask_about_coffee(menu, actual_resources)
    # make coffee and update machine resources
    make_coffee(coffee, coffee_ingredients, actual_resources)





def ask_about_coffee(menu, actual_resources):
    coffee = input("What would you like? (espresso/latte/cappuccino): ").strip()   
    if coffee in menu:
        # check if resources are aviable, returns True if resources are not enough
        if check_resources(menu[coffee]["ingredients"], actual_resources):
            return ask_about_coffee(menu, actual_resources)
        # ask user to insert coins and check if it is enough. If not ask about other coffee
        if ask_coin(menu[coffee]["cost"]):
            return ask_about_coffee(menu, actual_resources)
        return coffee, menu[coffee]["cost"], menu[coffee]["ingredients"]
    elif coffee == "report":
        for ingredient, quantity in actual_resources.items():
            print(f"{ingredient}: {quantity}")
    elif coffee == 'off':
        exit("Have a nice day!")
    return ask_about_coffee(menu, actual_resources)


# check if resources are enough to make the coffee
def check_resources(required_resources, actual_resources):
    for ingredient, quantity in required_resources.items():
        if quantity > actual_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return True


# return True if users coins input is not enough, otherwise False
def ask_coin(cost):
    print("Please insert coins.")
    total_value = 0
    total_value += coin_type('quarters')
    total_value += coin_type('dimes')
    total_value += coin_type('nickles')
    total_value += coin_type('pennies')
    if cost < total_value:
        print(f"Here is ${round((total_value - cost), 2)} in change.")
        return False
    else:
        print("Sorry that's not enough money. Money refunded.")
        return True



# ask user how many quarters he put
def coin_type(type):
    quantity = input(f"How many {type}?: ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            return 0
        elif type == "quarters":
            return round((quantity * 0.25), 2)
        elif type == "dimes":
            return round((quantity * 0.10), 2)
        elif type == "nickles":
            return round((quantity * 0.05), 2)
        elif type == "pennies":
            return round((quantity * 0.01), 2)
    except:
        return 0
        

# make coffee and update machine resource
def make_coffee(coffee, coffee_ingredients, actual_resources):
    print(f"Here is your {coffee} \U00002615")
    for ingredient, quantity in coffee_ingredients.items():
        actual_resources[ingredient] -= quantity
    main(actual_resources, introduction=False)



main()