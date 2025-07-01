import menu_res

def check_resources_sufficient(order, resource, earned_money):
    insert_coin = True
    for key, value in menu[order]["ingredients"].items():
        if resource[key] < value:
            print(f"Sorry there is not enough {key}.")
            insert_coin = False
    if insert_coin:
        print("Please insert coins.")
        resource, earned_money = process_coins(order, resource,earned_money)

    return resource, earned_money

def process_coins(order, resource, earned_money):
    cost = menu[order]["cost"]
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    insert_money = round(quarters + dimes + nickles + pennies,2)
    if insert_money < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        for key, value in menu[order]["ingredients"].items():
            resource[key] -= value
        return_money = insert_money - cost
        earned_money += cost
        print(f"Here is ${return_money} in change.")
        print(f"Here is your {order} ☕️. Enjoy!")

    return resource, earned_money


resources = menu_res.resources
menu = menu_res.MENU
money = 0

Off = False
while not Off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"money: ${money}")

    elif user_choice == "off":
        Off = True
    else:
        resources, money = check_resources_sufficient(user_choice,resources,money)
