#!/usr/bin/env python3

"""
DICTIONARY COMPREHENSION
"""

animalsEx = [{'a': 'ant'}, {'b': 'bear'}, {'c': 'cat'}, {'d': 'dog'}]
animals = {item[0]: item[1] for item in animalsEx}
print(animals)

animals = {key: value for key, value in animalsEx}
print(animals)
