#!/usr/bin/env python3

"""
SETS
"""

mySet = {'a', 'b', 'c'}
print(mySet)

mySet = set({'a', 'b', 'c'})
print(mySet)

mySet.add('d')  # To insert an element to the set
print(mySet)

mySet.pop()  # To remove a random elemnt from the set
print(mySet)

mySet.discard('a')  # To remove a specific element from the set
print(mySet)
