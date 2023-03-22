# Exercise-3: Write a Python program to display the current date and time.

import datetime
"""
now= datetime.datetime.now()
print("Current Date and Time:")
print(now.strftime("%y-%m-%d %H-%M-%S"))
print(now.strftime("%H-%M-%S"))
print(now.strftime("%y_%m_%d"))

# Exercise-4: Write a Python program that calculates the area of a circle based
# on the radius entered by the user.
from math import pi
r = float(input("enter the value of radious: "))
Area= pi*r**2
print("%.3f"% Area)


# Exercise-6: Write a Python program that accepts a sequence of comma-separated
# numbers from the user and generates a list and a tuple of those numbers.
number = (input("Enter the numbers: "))
number = number.split()
print("List: ",list(number))
print("Tuple:", tuple(number))


# Exercise-7: Write a Python program that accepts a filename from the user and
# prints the extension of the file.

filename= str(input("Enter the file name with extension- "))
file_ex = filename.split(".")
print("The extension of the file is: ",file_ex[1])


# Exercise-8: Write a Python program to display the first and last colors from the
# following list.
from operator import itemgetter
color_list = ["Red","Green","White" ,"Black"]
print(itemgetter (0,3) (color_list))
lst= color_list[0],color_list[3] # if print this directly then shows only the name without ()
print(list(lst))


#Exercise-9: Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
#date = exam_st_date.("/")
print("The examination will start from: %i/%i/%i"% exam_st_date)
"""

# Execcise-10: Write a Python program that accepts an integer (n) and
# computes the value of n+nn+nnn.

n= int(input("Enter an integer- "))
value= str(n)
n2= value+value
n3= value+value+value
total= n + int(n2) + int(n3)
print(total)