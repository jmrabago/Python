#!/usr/bin/env python3

"""
Ascii code
"""

base ='ale'
word = str(input('Iserta una palabra: '))

print(ord(word[0]))

#for letter in word:
 #   ascii_number = ord(letter)
  #  print(f'Ascii para {letter} es: {ord(letter)}')

chr_list = []

for i in range(len(word)):
    ascii_number = ord(word[i])
    print(f'Ascii para {word[i]} es: {ord(word[i])}')
    chr_list.append(chr(ascii_number + 1)) if ascii_number != 122 else chr_list.append('a') if ascii_number == 122 else chr_list.append(word[i])
    print(f'Nueva Ascii es: {ord(chr_list[i])}')

print(''.join(chr_list))

if word[0] == base[0]:
    print('La primera letra es igual a la base')

