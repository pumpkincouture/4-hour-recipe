from shopping_list_generator import ShoppingListGenerator
from mock import MagicMock
import unittest

class ShoppingListGeneratorTestClass(unittest.TestCase):
    def test_shopping_list_has_recipe_ingredients(self):
        recipe_list = [self.__create_salmon_recipe(), self.__create_chicken_recipe()]

        shopping_list = ShoppingListGenerator(recipe_list)

        transformed_list = [
                "Oven Baked Salmon": {
                    "Salmon": 8.00,
                    "Frozen Veggies": 2.00,
                    "Total": 10.00
                    },
                "Lemon Chicken": {
                    "Chicken": 4.50,
                    "Broccoli": 5.50,
                    "Lemon": 2.00,
                    "Total": 12.00
                    }
                ]


    def __create_salmon_recipe(self):
        salmon = MagicMock("Salmon", 1, 8.00)
        frozen_vegetables = MagicMock("Frozen Veggies", 2, 1.00)

        prep_time = 10
        cook_time = 20

        ingredients = [ salmon, frozen_vegetables ]

        return MagicMock("Oven Baked Salmon", ingredients, prep_time, cook_time)

    def __create_chicken_recipe(self):
        chicken = MagicMock("Chicken", 1, 4.50)
        broccoli = MagicMock("Broccoli", 3, 2.50)
        lemons = MagicMock("Lemon", 2, 1.00)

        prep_time = 10
        cook_time = 30

        ingredients = [ chicken, broccoli, lemons ]

        return MagicMock("Lemon Chicken", ingredients, prep_time, cook_time)

if __name__ == '__main__':
    unittest.main()
