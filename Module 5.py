"""
import random
import math



#exercise 1

dices = int(input(" Please enter the number of dices you'd like to roll: "))
total_sum = 0

for x in range(dices):
    y =  random.randint(1,6)
    total_sum += y


print (f"The total sum of dices is {total_sum}")

#exercise 2

num = []

while True:
    user_input = input(" Please enter a number(or press enter to quit): ")
    if user_input == "":
     break
    num.append(int(user_input))
    num.sort(reverse=True)

    top5 = num[:5]

    print(f"Sorted list is {top5}")

#exercise 3

number = int(input("Please enter an integer: "))

for x in range(2,number):
    if number % x == 0:
        print ("This integer isn't a prime number")
        break
    else:
        print("This number is a prime number")
        break
"""

#exercise 4

cities = []

for i in range(5):
    city = str(input("Please enter a city: "))
    cities.append(city)

print(cities)




