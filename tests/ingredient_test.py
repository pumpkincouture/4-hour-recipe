from ingredient import Ingredient
import unittest

class IngredientTestCase(unittest.TestCase):
    def test_ingredient_has_name(self):
        ingredient = Ingredient("Corn", 2, 1)
        self.assertEqual(ingredient.name, "Corn")

    def test_ingredient_has_quantity(self):
        ingredient = Ingredient("Corn", 2, 1)
        self.assertEqual(ingredient.quantity, 2)

    def test_ingredient_has_price(self):
        ingredient = Ingredient("Corn", 2, 2.35)
        self.assertEqual(ingredient.price, 2.35)

if __name__ == '__main__':
    unittest.main()
