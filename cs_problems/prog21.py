# Question 2

import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

currentYear = datetime.datetime.now().year
year = currentYear

while age <= 100:
  year += 1
  age += 1

print (f"Hey {name}, you will turn 100 in the year {year}!!")
