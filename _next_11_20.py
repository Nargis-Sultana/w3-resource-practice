"""
#Exercise-12: Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.
import calendar
y= int(input("Enter the year- "))
m= int(input("Enter the month- "))
print(calendar.month(y, m))


# Exercise-14: Write a Python program to calculate the number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)

from datetime import date
first_date = date(2016,11,20)
last_year = date(2022,10,27)
deff= last_year - first_date
print(deff.days)

# Exercise-15: Write a Python program to get the volume of a sphere with radius six.
from math import pi
r= 6
volume= 4/3*(pi*r**3)
print("Volume of the sphere is- ", "%.3f"% volume)

# Exercise-16: Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.
a= int(input("Enter a number- "))
b= 17
if a>b:
    print(2*(a-b))
else:
    print("B is greater")

def difference(n):
    if n>17:
        return 2*(n-17)
    else:
        return 17-n
n= int(input("Enter an integer- "))
print(difference(n))


# Exercise-17: Write a Python program to test whether a number is within 100 of 1000 or 2000.
# formula-1
n= int(input("Enter a number- "))
if n in range (900, 1100):
    print("The number is within 100 of 1000")
elif n in range (1900, 2100):
    print("The number is within 100 of 2000")
else:
    print("False")

# formula-2
start=0
end= int(input("Enter the end limit- "))
for n in range (end):
    def near_thousand (n):
        return (abs(1000-n)<=100) or (abs(2000-n)<=100)
    n= int(input("Enter a number- "))
    print (near_thousand(n))
    start+=1


#Exercise-18: Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.
#formula-1

num1 = int(input("Enter the 1st number- "))
num2 = int(input("Enter the 2nd number- "))
num3 = int(input("Enter the 3rd number- "))
if num1 == num2 == num3:
    print(3 * (num1+num2+num3))
else:
    print("The values are not equal")

# formula-2
def three_value(x, y, z):
    sum= x + y + z
    if x==y==z:
        sum= 3 * sum
    return sum
x= int(input("Enter the 1st number- "))
y= int(input("Enter the 2nd number- "))
z= int(input("Enter the 3rd number- "))
print(three_value(x, y, z))



#Exercise- 19: Write a Python program to get a newly-generated string from a given string
# where "Is" has been added to the front. Return the string unchanged
# if the given string already begins with "Is".
# formula-1
N= input("Enter a string- ")
if N[:2] == "Is":
    print(N)
else:
    print("Is"+N)

# formula-2

def given_string (s):
    if s[:2] == "Is":
        return s
    else:
        return "Is"+s
s= input("Enter a string- ")
print(given_string(s))
"""

# Exercise-20: Write a Python program that returns a string
# that is n (non-negative integer) copies of a given string.

def string_copy (s):
    if n>=0:
        s = s+ ""
        result= s * n
        return result
s= input("Enter a string- ")
n = int(input("Enter the number of copy- "))
print(string_copy(s))