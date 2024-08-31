import random

#exercise 1
def dice_roll():

    while True:
        dice = int(random.randint(1,6))
        print(dice)
        if dice == 6:
         break
        else:
            dice = int(random.randint(1,6))


#exercise 2
def modify_dice_roll(x):
    while True:
        dice = int(random.randint(1, x))
        print(dice)
        if dice == x:
            break
        else:
            dice = int(random.randint(1, x))



#exercise 3
def gallons_to_litres():

    gas = float(input("Please input your quantity of gallons: "))
    while True:
        if gas < 0:
            break
        litres = gas * 3.78
        print (litres)
        return litres


#exercise 4

#Write a function that gets a list of integers as a parameter.
#The function returns the sum of all the numbers in the list.
#For testing, write a main program where you create a list, call the function, and print out the value it returned.

def list_integer():






"""
dice_roll()
modify_dice_roll(78)
gallons_to_litres()
"""
