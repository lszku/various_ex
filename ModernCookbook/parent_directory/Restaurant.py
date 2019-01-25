"""
restauracja
waiter
    -name

order
    -orderings: list[orderings]
    -waiter
    -
position
ordering

dish

"""


class Waiter:
    def __init__(self, name: str):
        self.name = name


class Dish:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Order:
    def __init__(self, waiter: Waiter):
        self.waiter = waiter
        self.orderings = []

    def add_to_order(self, waiter: Waiter, dish: Dish, amount: int = 1):
        for i in range(amount):
            self.orderings.append(Ordering(dish, waiter))

    def create_receipt(self):
        return Recipe(self)


class Ordering:
    def __init__(self, dish: Dish, waiter: Waiter):
        self.dish = dish
        self.waiter = waiter


class Menu:
    def __init__(self):
        self.dishes = {}

    def add_to_menu(self, name: str, dish: Dish):
        self.dishes[name] = dish

    def get_dish(self, name: str):
        return self.dishes.get(name)


class Recipe:
    def __init__(self, order: Order):
        self.order = order
        self._recipe = self._submit_order(order)

    def _submit_order(self, order: Order):
        summary = 0
        for ordering in order.orderings:
            summary += ordering.dish.price

        return summary
