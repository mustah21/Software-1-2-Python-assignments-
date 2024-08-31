import random
import math

#exercise 1
def dice_roll():

    while True:
        dice = int(random.randint(1,6))
        print(dice)
        if dice == 6:
         break
        else:
            dice = int(random.randint(1,6))

dice_roll()


#exercise 2
def modify_dice_roll(x):
    while True:
        dice = int(random.randint(1, x))
        print(dice)
        if dice == x:
            break
        else:
            dice = int(random.randint(1, x))

modify_dice_roll(78)


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
def sum_num(integer):
    return sum(integer)

numbers = [12 , 5 , 23, 2]
print(sum_num(numbers))

gallons_to_litres()


#exercise 5
def list_integers(num):
        even_num = []
        for i in num:
            if i % 2 == 0:
                even_num.append(i)
        return even_num

my_list = [12, 4 , 7, 5, 10]
print ("Original list:", my_list)
print ("List with only even numbers: ", list_integers(my_list))


#exercise 6
def pizza(diameter, price):
    area = ((diameter/2)**2 * math.pi) * 0.0001
    unit_price = price/ area
    return unit_price

w = float(input("Enter your diameter in cm: "))
x = float(input("Enter your price: "))
y = float(input("Enter your diameter in cm: "))
z = float(input("Enter your price: "))

unit_price1 = pizza(w,x)
unit_price2 = pizza(y,z)

if unit_price1 > unit_price2:
    print("Pizza two is more value for money")
elif unit_price2 < unit_price1:
    print("Pizza one is more value for money")
else:
    print("Both have the same unit price")