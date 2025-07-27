#!/usr/bin/env python3

"""
Test
"""

myList = [1, 3, 5, 7, 8]
myList2 = [12, 9, 30]

print(myList)
print(myList[1])

for i in range(len(myList)):
    if i == len(myList) - 1:
        print(myList[i])

myList.append(3)

for i in range(len(myList)):
    if i == 3:
        myList[i] = 60

print(myList)
print(myList[1: 5])

myList.append(myList2)
print(myList)

myList.extend(myList2)
print(myList)
