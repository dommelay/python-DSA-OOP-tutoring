# SHOPPING WITH CLASSES AND OBJECTS

class Item:
    # Initialize an instance (object) of the Item class
    def __init__(self, name, cost, purchased):
        self.name = name
        self.cost = cost
        self.purchased = purchased
    # Purchase an item
    def purchase(self):
        self.purchased = True
        print(f'{self.name} purchased for ${self.cost}')
    # Display item details
    def display_item(self):
        print(f'Item: {self.name}')
        print(f'- Cost: ${self.cost}')
        print(f'- Purchased: {self.purchased}')     

class ShoppingList:
    # Initialize an instance (object) of the ShoppingList class
    def __init__(self, date, items):
        self.date = date
        self.items = items
    # Print each item on the shopping list
    def print_list(self):
        print(f'Shopping List for {self.date}')
        for item in self.items:
            print(f'- {item.name}, Cost: ${item.cost} Purchased: {item.purchased}')
    # Add an item to the shopping list
    def add_item(self, item):
        self.items.append(item)
        print(f'{item.name} added to the shopping list!')
    # Remove an item from the shopping list
    def remove_item(self, item):
        print(f'{item.name} removed from the shopping list.')
        self.items.remove(item)
       
# CREATE TWO ITEMS

# CREATE A SHOPPING LIST INCLUDING THE TWO ITEMS

# PRINT THE SHOPPING LIST

# PURCHASE ONE ITEM AND PRINT THE LIST

# CREATE A THIRD ITEM

# DISPLAY THE THIRD ITEM

# ADD THE THIRD ITEM TO THE SHOPPING LIST

# PRINT THE SHOPPING LIST
        
# REMOVE THE FIRST ITEM FROM THE SHOPPING LIST

# PRINT THE SHOPPING LIST






























# item1 = Item('Gold Chain', 50, False)
# item2 = Item('Red Bottoms', 75, False)
# item3 = Item('Puffer Jacket', 30, False)

# listA = ShoppingList('03/18/2024', [item1, item2])
# listA.add_item(item3)
# item1.purchase()
# listA.remove_item(item1)
# listA.print_list()
# item1.display_item()

