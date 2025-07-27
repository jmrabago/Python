#!/usr/bin/env python3

"""
DICTIONARIES
"""

from collections import defaultdict

# Creation of a dictionary
animals = {
    'a': 'ant',
    'b': 'bear',
    'c': 'cat'
}
print(animals)

animals['d'] = 'dog'  # How to insert new values to a dictionary
print(animals)

print(animals.keys())  # Get only the keys of the dictionary

print(animals.values())  # Get only the values of the dictionary

print(animals.get('a'))  # To retrieve an specific value by it's key

animals = {
    'a': ['ant', 'antilope'],
    'b': ['bear']
}
print(animals)

# Insert a new element to a list passed as a value in a dictionary
animals['b'].append('bug')
print(animals)

# To insert new key with a list as a value in a dictionary
if 'c' not in animals:
    animals['c'] = []

animals['c'].append('cat')
print(animals)

# Default Dict
# Syntax of a creation of a dictionary using defaultdict
animals = defaultdict(list)
animals['e'].append('elephant')
print(animals)
