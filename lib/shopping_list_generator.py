from shopping_list_item import ShoppingListItem

class ShoppingListGenerator:
    def __init__(self, recipe_list, price_calculator):
        self.recipe_list = recipe_list
        self.price_calculator = price_calculator

    def calculate_ingredients(self):
    	items = []
    	for recipe in self.recipe_list:
    		for ingredient in recipe.ingredients:
    			total = self.price_calculator.total_ingredient_price(ingredient.quantity, ingredient.price)  
    			items.append(ShoppingListItem(recipe.name, recipe.ingredients, total))

    	print items

    			