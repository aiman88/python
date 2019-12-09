"""
Author - Aiman
Date : 6/Dec/2019
Write a program which will find factors of given number and find whether the
factor is even or odd.
"""

given_number=9
sum=1

while given_number>0:
    sum=sum*given_number
    given_number-=1
print(sum)

if sum%10!=0:
    print("odd number")
else:
    print("Even number")



