#!/usr/bin/env python3

"""
IF AND ELSE
"""

# Including elif as an else if
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

# Single line if statements
i = 5
print('Fizz' if n % 3 == 0 else i)

fizzBuzz = 'Fizz' if n % 3 == 0 else i

print('FizzBuzz' if n % 15 == 0 else 'Fizz' if n %
      3 == 0 else 'Buzz' if n % 5 == 0 else i)
