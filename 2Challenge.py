# Created by Samuelito Perro
############################
# A program that calculates the longest word
# eliminating bad characters

import sys
import re
import string

sent = input ('Please enter a sentence: ')

#Checking for minimum words
if sent == "":
    print('Error: Please enter at least one word')
    sys.exit(0)

#veryfy words for special characters
table = str.maketrans(dict.fromkeys('~!@#$%^&*()_+=}{[]|;:<>,.\'`'))
sent = sent.translate(table)
    
#Split every word by spaces
wordsarr = sent.split(" ")

#Creating loop to compare with previous strings
Longest = wordsarr[0]
for i in wordsarr:
    if len(i) > len(Longest):
        Longest = i

print('The longest word entered was: ', Longest)

