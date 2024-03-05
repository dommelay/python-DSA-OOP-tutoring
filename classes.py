# print('hello world')

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def say_hello(self):
        return f'Hello {self.name}'

person = Person('Dominique', 25, 'San Francisco')
greeting = person.say_hello()
print(person.city)
print(greeting)