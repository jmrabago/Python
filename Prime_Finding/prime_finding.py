#!/usr/bin/env python3

"""
PRIME FINDING
"""

def allPrimesUpTo(num):
    primes = [2]

    for number in range(3, num):
        sqrtNum = number ** 0.5

        for factor in primes:
            if number % factor == 0:
                # Not prime
                break
            if factor > sqrtNum:
                # It's prime
                primes.append(number)
                break

    return primes


print(allPrimesUpTo(int('Inserta el número hasta el cual quieres encontrar los números primos: ')))
