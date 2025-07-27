#!/usr/bin/env python3

"""
FUNCTIONS
"""
import math


def sum(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(sum(1, 2))
print(multiply(3, 4))

# Named parameters
# Keyword arguments must come after positional arguments


def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2


print(performOperation(2, 3, operation='multiply'))

# *args


def performOperation(*args):
    print(args)


performOperation(1, 2, 3)


def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)


print(performOperation(2, 3, operation='multiply'))

# **kwargs


def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)


performOperation(1, 2, 3)

# Lambda functions
print((lambda x: x + 3)(5))

myList = [5, 4, 3, 2]
print(sorted(myList))

myList = [{'num': 3}, {'num': 2}, {'num', 1}]
print(sorted(myList, key=(lambda x: x['num'])))
