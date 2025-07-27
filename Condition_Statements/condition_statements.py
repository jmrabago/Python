#! /usr/bin/env python3

"""
If statement
"""

userInput = input('Enter 1 or 2: ')

if userInput == "1":
    print("Hello World")
    print("How are you")
elif userInput == "2":
    print("Python Rocks!")
    print("I love Python")
else:
    print("You did not enter a valid number")

#For loop
pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print(myPets)

for index, myPets in enumerate(pets):
    print(index, myPets)

message = 'Hello'

for i in message:
    print(i)

for i in range(5):
    print(i)

#While loop
counter = 5

while counter > 0:
    print("Counter = ", counter)
    counter = counter - 1

#Break
j =0

for i in range(5):
    j += 2
    print('i = ', i, ', j = ', j)
    if j == 6:
        break

#Continue
w = 0

for i in range(5):
    w += 2
    print('\ni = ', i, ', w = ', w)
    if w == 6:
        continue
    print('I will be skipped over if w=6')


#Try, except

try:
    answer = 12 / 0
    print(answer)
except:
    print("An error has occured")

try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer1 = userInput1 / userInput2
    print("The answer is ", answer1)
    myFile = open("missing.txt", 'r')
except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Unknown error: ", e)
