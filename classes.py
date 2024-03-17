# print('hello world')

class Person:
    #class variable
    species = 'Human'

    #initialize the object 
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    #object method
    def say_hello(self):
        return f'Hello {self.name}'
    
    #special object method/function to sefine string representation of a function
    def __str__(self):
        return f'Person(name={self.name}, age={self.age}, city={self.city})'

#create instances of the class
person = Person('Dominique', 25, 'San Francisco')
person1 = Person('Roman', 25, 'Los Angeles')
greeting = person.say_hello()

# print(person.name, person1.name)
# print(person1.say_hello())
#acess attributes
# print(person.city)
# print(greeting)
print(person)
print(person.__str__())