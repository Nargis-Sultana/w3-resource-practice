"""
# Exercise -21: Write a Python program that determines whether a given number
# (accepted from the user) is even or odd, and prints an appropriate message to the user.
#formula-1
num = int(input("Enter a number- "))
if num%2==0:
    print("The number is an even number")
else:
    print("The number is odd")

#formula-2

def even_odd (n:int):
    return "The given number is even" if n%2==0 else "The number is odd"
n= int(input("Enter an integer- "))
print(even_odd(n))

# Exercise-22: Write a Python program to count the number 4 in a given list.
# formula-1
def given_list(A_list):
    count = 0
    for num in A_list:
        if num == 4:
            count+=1
    return count
A_list= [0,1,4,3,5,4,6,4,33,44,88,7,4,4,4,5]
print(given_list(A_list))

# formula-2
A= [1,4,3,2,4,9,4,7]
count_num = []
for value in A:
    if value== 4:
        count_num.append(value)
print(len(count_num))

# formula-3

def count_four(B):
    return len ([value for value in B if value == 4])
B = str(input("Enter number of strings- "))
#B = list(strn_num)
#print(B)
print(count_four(list(B)))

# formula-4
A= [1,4,3,2,4,9,4,7]
print(A.count(4))

# exercise-23:Write a Python program to get n (non-negative integer) copies of the first 2 characters
# of a given string. Return n copies of the whole string if the length is less than 2.
def strng_copy(N):

    if len(N)<2:
        N= N +""
        return N * n
    else:
        return N[:2] * n
N= str(input("Write a string-"))
n= int(input("Enter the number of copy-"))
print(strng_copy(N))


# Exercise no- 24: Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(Letter):
    Vowel = "AEIOUaeiou"
    if Letter in Vowel:
        return "The letter is vowel"
    else:
        return "The letter is not vowel"
Letter = str (input("Enter a letter-"))
print(is_vowel(Letter))


# Exercise no-25: Write a Python program that checks whether a specified value is
# contained within a group of values.
#Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
# formula-1

A_list = [1,5,8,3]
value = int(input("Enter an integer- "))
if value in A_list:
    print ("The value is contained in the group")
else:
    print("Error: value is not in the group")

# formula-2

def check_number(lst,n):
    return n in lst
print(check_number([1,5,8,3], int(input("Search the number- "))))


# Exercise-26: Write a Python program to create a histogram from a given list of integers.
#formula-1
def histogram(value):
    for n in value:
        end = n
        result = ""
        while end>0:
            result+= "*"
            end = end -1
        print(result)
histogram([2,3,5,4])

#formula-2
def hist(x):
    y= "*"
    for i in range (len(x)):
        print (y*x[i])
hist([2,3,5,6])

#formula-3
lst= [3,4,5,6]
for i in lst:
    #n=i
    print("*"*i)


#Exercise-27: Write a Python program that concatenates all elements in a list into
# a string and returns it.
def list_concate(A_list):
    result= ""
    for value in A_list:
        result+= str(value)
    return result
A_list = [1,2,12,33]
print(list_concate(A_list))


# Exercise-28: Write a Python program to print all even numbers from a given list of numbers in the
# same order and stop printing any after 237 in the sequence.
# Sample numbers list :

# formula-1
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
           399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
           958,743, 527]
count_even = filter (lambda num: num%2==0, numbers)
print(list(count_even))

#formula-2
for i in numbers:
    if i==237:
        break
    elif i%2==0:
        print(i)


# Exercise-29: Write a Python program that prints out all colors from color_list_1
# that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
#formula-1

n= color_list_1.difference(color_list_2)
print(n)
a = color_list_2.difference(color_list_1)
print(a)
#formula-2

print(color_list_1 - color_list_2)

#formula-3
def get_color (x,y):
    return (x for x in color_list_1 if x not in color_list_2)
x = set(["White", "Black", "Red"])
y = set(["Red", "Green"])
print(set(get_color(x,y)))
"""

# Exercise-30: Write a Python program that will accept the base and height of
# a triangle and compute its area.
#formula-1

b= int(input("Write the base- "))
h= int(input("Input the height- "))
area = .5 * b* h
print(area)

#formula-2

area_of_triangle= lambda b,h:b*h/2
print(area_of_triangle(b=int(input()),h=int(input())))
