# components key has those values: water, coffee, milk
orders = {
    "espresso": {"price": 1.50, "components": [["water", 50], ["coffee", 18], ], },
    "latte": {"price": 2.50, "components": [["water", 200], ["coffee", 24], ["milk", 150], ], },
    "cappuccino": {"price": 3.00, "components": [["water", 250], ["coffee", 24], ["milk", 100], ], },
}

# resources are 0 :water, 1: coffee, 2: milk, 3: money
resources = [["water", 300, "ml"], ["coffee", 100, "g"], ["milk", 200, "ml"], ["money", 0, "$"], ]

machine_on = True

while machine_on:
    order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        machine_on = False
    elif order == 'report':
        # Todo: 3: when the word "report" entered within the prompt a report that shows how much resources left should
        #  be shown, water: milk: coffee: money:
        report = ""
        for resource in resources:
            resource_name = resource[0].capitalize()
            resource_value = resource[1]
            resource_unit = resource[2]
            if resource[0] == "money":
                report = f"\t{resource_name}: {resource_unit}{resource_value}"
            else:
                report = f"\t{resource_name}: {resource_value}{resource_unit}"
            print(report)
    elif order in orders.keys():
        # I'll check if the resources are enough to make the order
        index = 0
        sufficient_resources = True
        components = orders[order]['components']
        # Bellow i'll check if the resources are sufficient for the order
        for component in components:
            if resources[index][1] < component[1]:
                print(f"Sorry there is not enough {component[0].capitalize()}.")
                sufficient_resources = False
            index += 1

        # Bellow i'll ask for the order money, then check if it is enough.
        if sufficient_resources:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))  # equal to 0.25
            dimes = int(input("how many dimes?: "))  # equal to 0.10
            nickles = int(input("how many nickles?: "))  # equal to 0.05
            pennies = int(input("how many pennies?: "))  # equal to 0.01
            money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
            order_price = orders[order]['price']
            if money >= order_price:
                change = money - order_price
                formatted_change = "{:.2f}".format(change)
                print(f"Here is ${formatted_change} in change.")
                print(f"Here is your {order} ☕. Enjoy!")

                # I'll add the money to the cash, and deduct the order components from the resources.
                # Money
                resources[3][1] += order_price
                # resources
                index = 0
                for component in components:
                    resources[index][1] -= components[index][1]
                    index += 1
            else:
                print("Sorry that's not enough money. Money refunded.")
