import file_parser
    
def make_all_drinks(coffee_machine, drinks):
    for drink in drinks:
        print(coffee_machine.make_drink(drink))

def check_status_after_every_drink(coffee_machine, drinks):
    for drink in drinks:
        print(coffee_machine.make_drink(drink))
        print(coffee_machine.low_ingredients_status())

def make_one_drink_n_times(coffee_machine, drink, n):
    for i in range(n):
        print(coffee_machine.make_drink(drink))

filename = input("Please enter the input JSON filename (eg 'input_1.json'):")

print(f"Reading file {filename}")
coffee_machine, drinks = file_parser.parse_input_file(filename)
print(f"Created a new coffee machine and read drinks' recipes from {filename}\n")
print("Checking ingredients' status\n")
print(coffee_machine.low_ingredients_status())
print("\nMaking all drinks\n")
make_all_drinks(coffee_machine, drinks)

print("\n")
coffee_machine, drinks = file_parser.parse_input_file(filename)
print("Created a new coffee machine\n")
print("Making every drink and checking ingredient status afterwards\n")
check_status_after_every_drink(coffee_machine, drinks)


print("\n")
coffee_machine, drinks = file_parser.parse_input_file(filename)
print("Created a new coffee machine\n")
print("Making first drink 5 times\n")
make_one_drink_n_times(coffee_machine, drinks[0], 5)

print("\nRefilling ingredients")
print(coffee_machine.add_ingredient("green_mixture", 200))
print(coffee_machine.add_ingredient("green_mixture", 200))
print(coffee_machine.add_ingredient("hot_water", 500))
print(coffee_machine.add_ingredient("hot_milk", 500))
print(coffee_machine.add_ingredient("hot_water", 50))
print(coffee_machine.add_ingredient("sugar_syrup", 200))

print("\nTrying to make all drinks again\n")
make_all_drinks(coffee_machine, drinks)









        
    
