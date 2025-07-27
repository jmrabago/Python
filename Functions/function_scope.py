#!/usr/bin/env python3

"""
FUNCTION SCOPE
"""

def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)


performOperation(1, 2, 'sum')

# locals()


def performOperation(num1, num2, operation='sum'):
    print(locals())


performOperation(1, 2, operation='multiply')

# globals()
globals()

# Global and Local scope
message = 'Some global data.'


def function1(varA, varB):
    print(message)
    print(locals())


def function2(varC, varB):
    print(locals())


function1(1, 2)
function2(3, 4)
