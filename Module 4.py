import math
import random
from itertools import count

"""

#exercise 1

number = 1

while number > 1000:
    if number % 3 == 0:
        print(number)
        number += 1

#exercise 2

centimeters = float(input("Enter your value: "))

while centimeters > 0:
    inches = centimeters * 0.393701
    print(inches)
    break
    

#exercise 3

largest = 0
smallest = 0

number = int(input("Enter your number: "))
if number != "":
        smallest = largest = number
while number != "":

    if number < smallest:
        smallest = number
    elif number > largest:
        largest = number

    number = int(input("Enter your number: "))
print(largest & smallest)


#exercise 4


number = random.randint(1,1000)

while True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed the correct number! {guess}")
        break
    elif guess < number:
        print("Your guess is too low!")
    elif guess > number:
        print ("Your guess is too high!")


#exercise 5

fix_username = str("python")
fix_password = str("rules")
attempts = 0


while attempts < 5:
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    if username == fix_username and password == fix_password:
        print ("        Welcome!")
        break
    else:
        if username != fix_username or password != fix_password:
             print("Please try again")
        attempts +=1
if attempts == 5:
    print ("Access Denied")

"""
#exercise 6