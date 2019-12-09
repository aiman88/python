'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

name = input("Please input your name :")
age_now = int(input("Please input your age :"))

year_now = 2019
balance_year = 100 - age_now
year_in_hundred = year_now + balance_year


print (f"Hi {name}, in {year_in_hundred} you will be 100 years old")