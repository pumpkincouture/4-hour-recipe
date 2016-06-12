from recipe import Recipe
from mock import MagicMock
import unittest

class RecipeTestCase(unittest.TestCase):
    def test_recipe_has_name(self):
        salmon = MagicMock("Salmon", "1", "10")
        ingredients = [salmon]
        prep_time = 10
        cook_time = 15

        recipe = Recipe("Oven Baked Salmon", ingredients, prep_time, cook_time)
        self.assertEqual(recipe.name, "Oven Baked Salmon")

    def test_recipe_has_ingredients(self):
        salmon = MagicMock("Salmon", "1", "10")
        ingredients = [salmon]
        prep_time = 10
        cook_time = 15

        recipe = Recipe("Oven Baked Salmon", ingredients, prep_time, cook_time)
        self.assertEqual(recipe.ingredients, ingredients)

if __name__ == '__main__':
    unittest.main()
