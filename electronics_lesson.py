# print('hello world')

class Device:
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
    def display_info(self):
        print(f'Device: {self.brand} {self.model}, {self.year}')

class Phone(Device):
    def __init__(self, brand, year, model, carrier):
        super().__init__(brand, year, model)
        self.carrier = carrier
    def display_info(self):
        super().display_info()
        print(f'Service provided by: {self.carrier}')
    def make_call(self, person):
        print(f'Ring Ring! Calling my good friend {person} from my {self.model}')
    def pay_carrier(self, paid, owed):
        leftover = owed - paid
        print(f'Thank you for paying ${paid} towards your bill with {self.carrier}!')
        print(f'You now owe ${leftover}')
class Laptop(Device):
    def __init__(self, brand, year, model, storage):
        super().__init__(brand, year, model)
        self.storage = storage
    def display_info(self):
        super().display_info()
        print(f'Storage Space: {self.storage}GB')
    def use_storage(self, amount):
        print(f'Using {amount}GB of storage!')
        self.storage -= amount
        print(f'Your {self.model} has {self.storage}GB left')

device1 = Laptop('Apple', 2023, 'MacBook', 500)
device2 = Phone('Apple', 2014, 'iPhone 13', 'T-Mobile')
# device2.display_info()
# device2.make_call()
# device1.use_storage(100)
# device2.make_call('Dominique')
# device2.pay_carrier(20, 100)
