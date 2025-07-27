#! /usr/bin/env python3

"""
CLASSES
"""

# Creation of a class
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('A dog barks.')


# Instance of an object of a class
my_dog = Dog('Lucas')
# Callling a method of the class
my_dog.speak()
# Calling a variable of the instnace
print(my_dog.name)

# Static attributes


class Dog:
    _legs = 4  # This is a static attribute, you need to develop a method to get the value

    def __init__(self, name):
        self.name = name

    def speak(self):
        print('A dog barks.')

    def getLegs(self):
        return self._legs


dog = Dog('Rover')
print(dog.name)
print(Dog._legs)
print(dog.getLegs())
