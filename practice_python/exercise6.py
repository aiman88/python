"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

word=input("Please enter word :")

reserve_word = ''
for i in word:
    reserve_word = i + reserve_word  # appending chars in reverse order

if word==reserve_word:
    print(f"{word} is a palindrome word")
else:
    print(f"{word} is not a palindrome word")



