from coffee_machine_data import MENU, profit, resources

def is_resources_sufficient(order_ingredients):
    ''' This returns if your order can be met or not by the ingredients left'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def coins():
    '''This returns the total money I owe for the coffee.'''
    print("Please insert coins")

    total = int(input("how many quarters? "))*0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total
def is_transaction_successful(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment-drink_cost,2)
        print(f"your change is ${change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")



is_on = True

while is_on :

    choice = input("What would you like to have ? (espresso\latte\cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"profit: {profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

