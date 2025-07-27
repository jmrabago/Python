#!/usr/bin/env python3

"""
ART ENCODING
"""

def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count += 1
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr += item[0] + item[1]
    return decodedStr

# Tests
print(encodeString('AAAAABBBBCCC'))
print(decodeString([('A', 5), ('B', 4), ('C', 3)]))
