MENU = {
    "espresso": {
        "ingredients": {
            "water": 50
            ,"coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200
            ,"milk": 150
            ,"coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250
            ,"milk": 100
            ,"coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300
    ,"milk": 200
    ,"coffee": 100
    ,"money" : 0
}

is_on = True
while is_on:

    # TODO 1: always being ready to take an order for the next customer
    choice = input("Hi there, what would you take today?\n")


    # TODO 2: Turn off by printing "off"
    if choice == "off":
        print("Goodbye World !")
        is_on = False

    # TODO 3: print a report of the amount of ingredients/money left in the machine when printing "report"
    elif choice == "report":
        for f in resources:
            if f == "water" or f == "milk":
                print(f"{f.capitalize()} : {resources[f]}ml")
            elif f == "coffee":
                print(f"{f.capitalize()} : {resources[f]}g")
            elif f == "money":
                print(f"{f.capitalize()} : ${resources[f]}")
            else:
                print("Error in report choice")

    # TODO 4: is there enough resources to make the coffee?
    elif choice in MENU:
        stop = False
        for f in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"][f] > resources[f]:
                print(f"Sorry there is not enough {f}.")
                stop = True

        # TODO 5: processing coins/ calculating -> giving back change
        if not stop:
            print("Please insert coins")
            quarters = float(input("quarters :  "))
            dimes = float(input("dimes :  "))
            nickles = float(input("nickels :  "))
            pennies = float(input("pennies :  "))
            total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

            # TODO 6: is the order successful? if not enough money -> reset and give back money, same for resources
            if MENU[choice]["cost"] > total:
                total = 0
                print("Sorry that's not enough money. Money refunded\n")

            else:
                # TODO 7: make the coffee and keeping the ingredients to date
                resources["money"] += total

                for f in MENU[choice]["ingredients"]:
                    resources[f] -= MENU[choice]["ingredients"][f]

                if total > MENU[choice]["cost"]:
                    resources["money"] -= total - MENU[choice]["cost"]
                    print(f"Here is ${(total - MENU[choice]['cost']):.2f} in change.")

                # TODO 8: "here is your {drink}. Enjoy !.
                print(f"Here is your {choice}. Enjoy !\n")
        else:
            print("\n")
    else:
        print("Wrong input, please try again.\n")






