"""
# Exercise-11: Write a Python program to print the documents
# (syntax, description etc.) of Python built-in function(s).
number= "syntax", "descrition"
print (abs.__doc__)


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
"""
def difference(n):
    if n>17:
        return 2*(n-17)
    else:
        return 17-n
n= int(input("Enter an integer- "))
print(difference(n))