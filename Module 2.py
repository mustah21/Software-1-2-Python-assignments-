import math
import random
"""

#exercise 1

name = input("Enter your name: ")
print (f"Hello" , name)

#exercise 2
r = float(input("Enter your radius"))
area = 3.142 * r * r

print("Your area is", area)

#exercise 3

Length = float(input("Enter your length"))
width = float(input("Enter your width"))

perimeter = 2*Length + 2*width
area = Length * width

print(f"Your perimeter is:", perimeter)
print(f"Your area is:", area)

#exercise 4

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
num3 = int(input("Enter a number"))

print (f"your sum is: {num1 + num2 + num3}, product is {num1 * num2 * num3}, average is {(num1 + num2 + num3)/3}")
"""

#exercise 5
talents = float(input("Enter your number of talents"))
lots = float(input("Enter your number of lots"))
pounds = float(input("Enter your number of pounds"))

kilogram = ((talents*20 + pounds )*32 + lots)*0.0133
grams = (kilogram - int(kilogram))*1000

print (f"The weight in modern units is {int(kilogram)} and {grams:.2f} grams")


#exercise 6

print (f"First lock number {random.randint(0,999):03d}")
second_lock = str(random.randint(1 , 6)) + str(random.randint(1 , 6)) + str(random.randint(1 , 6)) + str(random.randint(1 , 6))

print ("second lock is " + second_lock)