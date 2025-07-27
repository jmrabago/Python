#!/usr/bin/env python3

"""
INHERITANCE
"""

class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says: Bark!')

    def getLegs(self):
        return self.legs


class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap! Yap! Yap!')

    def wagTail(self):
        print('Vigorous wagging!')


dog = Chihuahua('Rover')
dog.speak()
dog.wagTail()

myDog = Dog('Lucas')
myDog.speak()

# Extending built-in classes
myList = list()


class UniqueList(list):
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List'

    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(1)

print(uniqueList)
