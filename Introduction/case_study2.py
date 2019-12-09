"""
Author - Aiman
Date : 6/Dec/2019
Write a code which accepts a sequence of words as input and prints the words in a
sequence after sorting them alphaabetically.
"""

str = input("Please Enter Words : ali ahmad abu ")

#breakdown the string into a list
words = str.split()

words.sort()

print("The sorted words are:")
for word in words:
    print(word)
