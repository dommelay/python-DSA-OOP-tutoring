class Device:
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
    def display_info(self):
        print(f'- Device: {self.brand} {self.model}, {self.year}')

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

class Headphones(Device):
    def __init__(self, brand, year, model, songs):
        super().__init__(brand, year, model)
        self.songs = songs
    def display_info(self):
        print('HEADPHONE OVERRIDE')
    def add_song(self, song):
        self.songs.append(song)
    def display_playlist(self):
        print('Playlist:')
        for song in self.songs:
            print(f'- {song}')


# CREATE TWO DEVICES - LAPTOP AND PHONE

# DISPLAY INFORMATION ABOUT YOUR LAPTOP
        
# DISPLAY INFORMATION ABOUT YOUR PHONE
            
# DISPLAY INFORMATION ABOUT YOUR HEADPHONES
        
# CALL A FRIEND USING YOUR PHONE
        
# USE STORAGE SPACE ON YOUR LAPTOP

# PRINT YOUR HEADPHONES PLAYLIST
            
# ADD A SONG TO YOUR PLAYLIST AND PRINT AGAIN
        
# PAY YOUR PHONE BILL


































# device1 = Laptop('Apple', 2023, 'MacBook', 500)
# device2 = Phone('Apple', 2014, 'iPhone 13', 'T-Mobile')
# device3 = Headphones('Bose', 2022, 'QC45', ['See Through', 'Kills', 'War'])
# device2.display_info()
# device2.make_call()
# device1.use_storage(100)
# device2.make_call('Dominique')
# device2.pay_carrier(20, 100)
