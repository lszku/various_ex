from ModernCookbook.parent_directory.Restaurant import Waiter, Order, Menu, \
    Dish


def get_menu():
    menu = Menu()
    menu.add_to_menu('schabowy', Dish('Schabowy', 15))
    menu.add_to_menu('muchomorowa', Dish('Muchomorowa zupa', 12))
    menu.add_to_menu('kawa z pianka', Dish('Kawa z pianka', 8))
    return menu


def test_create_order():
    menu = get_menu()
    john = Waiter('John')
    order1 = Order(john)
    order1.add_to_order(john, menu.get_dish('schabowy'))
    order1.add_to_order(john, menu.get_dish('kawa z pianka'))
    recipe = order1.create_receipt()

    assert recipe._recipe == 23
    assert len(order1.orderings) == 2
