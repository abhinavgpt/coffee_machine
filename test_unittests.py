import file_parser
import pytest

@pytest.fixture
def get_cm_drinks():
    input_file = "input_1.json"
    (coffee_machine, drinks) = file_parser.parse_input_file(input_file)
    return (coffee_machine, drinks)

def test_initialisation(get_cm_drinks):
    coffee_machine, drinks = get_cm_drinks
    assert(coffee_machine._outlets == 3)
    assert(len(coffee_machine._ingredients) == 5)
    ingredients =  { 'hot_water': 500,
                     'hot_milk': 500,
                     'ginger_syrup': 100,
                     'sugar_syrup': 100,
                     'tea_leaves_syrup': 100 }
    assert(coffee_machine._ingredients == ingredients)
    assert(len(drinks) == 4)

def test_make_drinks(get_cm_drinks):
    coffee_machine, drinks = get_cm_drinks
    drinks_mapping = {}
    for drink in drinks:
        drinks_mapping[drink.name] = drink
    for name in ["hot_tea", "hot_coffee"]:
        drink = drinks_mapping[name]
        assert(coffee_machine.make_drink(drink) == f"{drink.name} is prepared")
        
    green_tea_drink = drinks_mapping["green_tea"]
    assert(coffee_machine.make_drink(green_tea_drink).startswith(f"{green_tea_drink.name} cannot be prepared"))
    
def test_add_ingredients(get_cm_drinks):
    coffee_machine, drinks = get_cm_drinks
    assert(coffee_machine.add_ingredient('hot_water', 100) == "Item hot_water added."+\
                                                               " New quantity is 600")
    assert(coffee_machine.add_ingredient('new_ingred', 5) == "Item new_ingred added."+\
                                                               " New quantity is 5")
    
def test_status(get_cm_drinks):
    coffee_machine, drinks = get_cm_drinks
    assert(coffee_machine.low_ingredients_status() == "Ingredients are present in sufficient quantity")
    coffee_machine.make_drink(drinks[0])
    coffee_machine.make_drink(drinks[1])
    assert(coffee_machine.low_ingredients_status().startswith("These ingredients are in low quantity"))
    