#!/usr/bin/env python3

"""
LISTS
"""

# Slicing lists
myList = [1, 2, 3, 4, 5]
print(myList[0: 2])
print(myList[:: 2])

myList = list(range(100))
print(myList[:: 10])

# Modifying lists
myList = [1, 2, 3, 4]
print(myList)

myList.append(5)  # To insert a new value at the end
print(myList)

# To insert a new value in a specific position list.insert(position, newValue)
myList.insert(3, 'new value')
print(myList)

# Removes a specific value in the list, if it exists
myList.remove('new value')
print(myList)

myList.pop()  # Removes the last value of the list
