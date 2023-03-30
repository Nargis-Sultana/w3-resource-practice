#Exercise-31 and 32: Write a Python program that computes the greatest common divisor (GCD) and
# least common multiple (LCM)  of two positive integers.
import math
x = int(input("Enter a number- "))
y = int(input("Enter other number- "))
gcd_num= math.gcd(x,y)
print(gcd_num)
lcm_num= math.lcm(x,y)
print(lcm_num)