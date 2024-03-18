class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + ". My age is " + str(self.age))

    def work(self):
        print("Boring...")

class SuperHero(Person): # tell it to inherit from Person
    def __init__(self, name, age, powers):
        super().__init__(name,age) # call Person's __init__()
        self.powers = powers

    def greet(self):
        super().greet() # call Person's greet()
        self.listPowers()

    def listPowers(self):
        for power in self.powers:
            print(power)

    def work(self): # override Person's work()
        print("To action!")

superman = SuperHero('Clark Kent', 200, ['flight', 'strength', 'invulnerability'])
person1 = Person('Brian', 25)
# captainAmerica = SuperHero(person1, ['flight', 'jump'])


# person1.greet()
# superman.greet()
# superman.listPowers()
# superman.work()
# person1.work()

