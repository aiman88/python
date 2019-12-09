'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
'''
import random

Start = 0
Stop = 100
limit = 10

a = [random.randint(Start, Stop) for iter in range(limit)]
b = [random.randint(Start, Stop) for iter in range(limit)]

#a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

for i in a:
    if i in b and i not in c:
        c.append(i)
print(a)
print(b)
print(c)