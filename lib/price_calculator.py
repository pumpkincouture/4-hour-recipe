class PriceCalculator:
    def total_ingredient_price(self, quantity, price):
        return quantity * price

    def add_ingredient(self, quantity, price, total):
        new_ingredient_price = self.total_ingredient_price(quantity, price)

        return self.__additive_price(total, new_ingredient_price)

    def remove_ingredient(self, quantity, price, total):
        new_ingredient_price = self.total_ingredient_price(quantity, price)

        return self.__redactive_price(total, new_ingredient_price)

    def sum_total(self, prices):
        return sum(prices)

    def __additive_price(self, total_price, adjustment):
        return total_price + adjustment

    def __redactive_price(self, total_price, adjustment):
        return total_price - adjustment

