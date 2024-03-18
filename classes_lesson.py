# SHOPPING WITH CLASSES AND OBJECTS

class Item:
    # create an instance (object) of the Item class
    def __init__(self, name, cost, purchased):
        self.name = name
        self.cost = cost
        self.purchased = purchased
    # purchase an item
    def purchase(self):
        self.purchased = True
        # print(f'{self.name} purchased for ${self.cost}')
    # display an item
    def display_item(self):
        print(f'Item: {self.name}')
        print(f'- Cost: ${self.cost}')
        print(f'- Purchased: {self.purchased}')     

class ShoppingList:
    # create an instance (object) of the ShoppingList class
    def __init__(self, date, items):
        self.date = date
        self.items = items
    # print the each item on the shopping list
    def print_list(self):
        print(f'Shopping List for {self.date}')
        for item in self.items:
            print(f'- {item.name}, Cost: ${item.cost} Purchased: {item.purchased}')
    # add items to the shopping list
    def add_item(self, item):
        self.items.append(item)
        print(f'{item.name} added to the shopping list!')
    # remove items from the shopping list
    def remove_item(self, item):
        print(f'{item.name} removed from the shopping list.')
        self.items.remove(item)
       

# CREATE TWO ITEMS
item1 = Item('Milk', 5, False)
item2 = Item('Bread', 6, True)

# CREATE A SHOPPING LIST INCLUDING THE TWO ITEMS
listA = ShoppingList('01/01/2024', [item1, item2])

# PRINT THE SHOPPING LIST
# listA.print_list()

# PURCHASE ONE ITEM AND PRINT THE LIST
item1.purchase()
# listA.print_list()

# CREATE A THIRD ITEM
item3 = Item('Apple', 2, False)

# DISPLAY THE THIRD ITEM
# item3.display_item()

# ADD THE THIRD ITEM TO THE SHOPPING LIST
listA.add_item(item3)

# PRINT THE SHOPPING LIST
# listA.print_list()

# REMOVE THE FIRST ITEM FROM THE SHOPPING LIST
listA.remove_item(item1)

# PRINT THE SHOPPING LIST
listA.print_list()






























# item1 = Item('Gold Chain', 50, False)
# item2 = Item('Red Bottoms', 75, False)
# item3 = Item('Puffer Jacket', 30, False)

# listA = ShoppingList('03/18/2024', [item1, item2])
# listA.add_item(item3)
# item1.purchase()
# listA.remove_item(item1)
# listA.print_list()
# item1.display_item()

