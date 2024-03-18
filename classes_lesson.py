
print('hello, world!')

class Item:
    # create an instance (object) of the Item class
    def __init__(self, name, cost, purchased):
        self.name = name
        self.cost = cost
        self.purchased = purchased
    # purchase an item
    def purchase(self):
        self.purchased = True
        print(f'{self.name} purchased for {self.cost}')
        
class ShoppingList:
    # create an instance (object) of the ShoppingList class
    def __init__(self, date, items):
        self.date = date
        self.items = items
    # print the each item on the shopping list
    def print_list(self):
        print(f'Shopping List for {self.date}')
        for item in self.items:
            print(f'- {item.name}, Cost: ${item.cost}, Purchased: {item.purchased}')
    def add_item(self, item):
        self.items.append(item)
        print('New item added to shopping list!')

item1 = Item('Gold Chain', 50, False)
item2 = Item('Red Bottoms', 75, False)
item3 = Item('Puffer Jacket', 30, False)

listA = ShoppingList('03/18/2024', [item1, item2])
listA.add_item(item3)
# item1.purchase()
listA.print_list()
