#!/usr/bin/env python3

"""
LIST COMPREHENSION
"""

myList = [1, 2, 3, 4, 5]
print([2 * item for item in myList])  # To double each element of the list

# With filters
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
print(filteredList)

# With functions
myString = 'My name is Jose Manuel. I live in Guadalajara'
print(myString.split('.'))
print(myString.split())


def cleanWord(word):
    return word.replace('.', '').lower()


print(([cleanWord(word) for word in myString.split()]))

# Nested list
print([[cleanWord(word) for word in sentence.split()]
      for sentence in myString.split('.')])
