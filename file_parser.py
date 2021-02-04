import json
from models import CoffeeMachine, Drink

def parse_input_file(filename):
    with open(filename, 'r') as fh:
        data = json.load(fh)
        machine = data['machine']
        n_outlets = machine['outlets']['count_n']
        initial_ingredients = machine["total_items_quantity"]
        coffee_machine = CoffeeMachine(n_outlets, initial_ingredients)
        
        beverages = machine['beverages']
        beverages_list = []
        
        for beverage_name in beverages:
            ingredients = beverages[beverage_name]
            beverages_list.append(Drink(beverage_name, ingredients))
        
        return coffee_machine, beverages_list


            
            
            
        
