#!/usr/bin/env python3

"""
Data Types
"""

brand = 'Apple'
exchangeRate = 1.235235245

message1 = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' % (
    brand, 1299, exchangeRate)
message2 = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format(
    'Apple', 1299, 1.235235245)
message3 = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format(
    'Apple', 1299, 1.235235245)

print(message3)

# declaring the list, list elements can be of different data types
myList = [1, 2, 3, 4, 5, 'Hello']
# print the entire list.
print(myList)
# You’ll get [1, 2, 3, 4, 5, “Hello”]
# print the third item (recall: Index starts from zero).
print(myList[2])
# You’ll get 3
# print the last item.
print(myList[-1])
# You’ll get “Hello”

# assign myList (from index 1 to 4) to myList2 and print myList2
myList2 = myList[1:5]
print(myList2)
# You’ll get [2, 3, 4, 5]
# modify the second item in myList and print the updated list
myList[1] = 20
print(myList)
# You’ll get [1, 20, 3, 4, 5, 'Hello']

# append a new item to myList and print the updated list
myList.append("How are you")
print(myList)
# You’ll get [1, 20, 3, 4, 5, 'Hello', 'How are you']

# remove the sixth item from myList and print the updated list
del myList[5]
print(myList)
# You’ll get [1, 20, 3, 4, 5, 'How are you']”
