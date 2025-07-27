#!/usr/bin/env python3

"""
DATA STRUCTURES
"""

# Lists
myList = [1, 'Jose', True, 'Manuel', 68]  # Syntax of a creation of a list
print(len(myList))
print(myList)
myList.append(False)  # How to insert a new element to a list
print(myList)

# Sets
mySet = {1, 1, 'Rabago', 55, False}  # Syntax of a creation of a set
print(len(mySet))
print(mySet)
mySet.add(3)  # How to insert a new element to a set
print(mySet)

# Tuples
myTuple = (6, 'Fernandez', True, 23)  # Syntax to create a tuple
print(myTuple)

# Dictionaries
myDictionary = {
    'apple': 'red',
    'banana': 'yellow',
    'number': 6
}  # Syntax to create a dictionary
print(myDictionary['apple'])
print(myDictionary['number'])
print(myDictionary)
myDictionary['number2'] = 7  # How to add a new key, value to a dictionary
print(myDictionary)
