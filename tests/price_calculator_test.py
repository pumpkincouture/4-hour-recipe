from price_calculator import PriceCalculator
import unittest

class PriceCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = PriceCalculator()

    def test_total_price_of_ingredient(self):
        quantity = 2
        price = 2.10

        total = 4.20

        total_price = self.calculator.total_ingredient_price(quantity, price)

        self.assertEqual(total_price, total)

    def test_total_price_after_ingredient_is_added(self):
        new_quantity = 1
        item_price = 1.50
        original_total = 3.00

        new_total = 4.50

        updated_price = self.calculator.add_ingredient(new_quantity, item_price, original_total)

        self.assertEqual(updated_price, new_total)

    def test_total_price_after_ingredient_is_removed(self):
        quantity = 2
        item_price = 3.00
        original_total = 8.00

        new_total = 2.00

        updated_price = self.calculator.remove_ingredient(quantity, item_price, original_total)

        self.assertEqual(updated_price, new_total)

    def test_total_price_of_list(self):
        prices = [ 2.00, 3.00, 4.50, 1.10 ]

        expected_total = 10.60

        total_price = self.calculator.sum_total(prices)

        self.assertEqual(total_price, expected_total)

if __name__ == '__main__':
    unittest.main()
