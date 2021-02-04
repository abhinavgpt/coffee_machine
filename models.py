import threading

# This value will be used as a threshold for ingredient quantity to be marked as low
INGREDIENT_LOW_QUANTITY = 50

class Drink:
    """
    Class to model a Drink with its name and ingredients
    """
    def __init__(self, name: str, ingredients: dict):
        self.name = name
        self.ingredients = ingredients
    

class CoffeeMachine:
    """
    Class to model a Coffee Machine and its behaviors
    """
    def __init__(self, n_outlets: int, initial_ingredients: dict):
        self._outlets = n_outlets
        # Using a simple hashmap to store ingredients
        self._ingredients = initial_ingredients
        self._current_orders = 0
        self._lock = threading.Lock()
        
    def make_drink(self, drink: Drink):
        """
        Makes a drink. Checks for the availability of outlets and ingredients before
        making the drink
        
        Inputs: drink -> An object of Drink type
        Returns: A status message
        """
        # Checking if all outlets are busy
        if self._current_orders == self._outlets:
            return "No free outlet. Please try after some time"
        
        # Acquiring the lock to manage concurrent access to outlets and ingredients
        with self._lock:
            self._current_orders += 1
            
            # Checking if all required ingredients are available
            for ingred in drink.ingredients:
                if ingred not in self._ingredients:
                    self._current_orders -= 1
                    return f"{drink.name} cannot be prepared because {ingred}"+\
                            " is not available"
                            
            # Checking if all required ingredients are present in sufficient quantities
            for ingred in drink.ingredients:
                if self._ingredients[ingred] < drink.ingredients[ingred]:
                    self._current_orders -= 1
                    return f"{drink.name} cannot be prepared because item {ingred}"+\
                            " is not sufficient"
            
            # Reducing the ingredients' quantities by the drink made
            for ingred in drink.ingredients:
                self._ingredients[ingred] -= drink.ingredients[ingred]
            
            self._current_orders -= 1
            return f"{drink.name} is prepared"
    
    def add_ingredient(self, ingred: str, quantity: int):
        """
        To increase the quantity of an ingredient
        If ingredient is not available it will be added to the list
        Inputs: ingred: A str containing the ingredient name
                   qty: An integer containing the quantity to be added
        Returns: A status message
        """
        self._ingredients[ingred] = self._ingredients.get(ingred, 0) + quantity
        return f"Item {ingred} added. New quantity is {self._ingredients[ingred]}"
    
    def low_ingredients_status(self):
        """
        Returns a status message showing if ingredients are available above
        the threshhold quantity defined as INGREDIENT_LOW_QUANTITY
        """
        low_quantity = []
        for ingred in self._ingredients:
            if self._ingredients[ingred] < INGREDIENT_LOW_QUANTITY:
                low_quantity.append(ingred)
        if low_quantity:
            ingreds_joined = ", ".join(ingred for ingred in low_quantity)
            return "These ingredients are in low quantity: " + ingreds_joined
        
        return "Ingredients are present in sufficient quantity"