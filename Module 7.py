
"""
#exercise 1

seasons = ("spring", "summer", "autumn", "winter")
month_number = int(input("Enter the number of the month to find the season: "))
month_corrected = month_number-1

if month_corrected == 11 or month_corrected <= 1:
    print(seasons[3])
elif 1 < month_corrected <= 4:
     print(seasons[0])
elif 4 < month_corrected <= 7:
    print(seasons[1])
elif 7 < month_corrected <= 10:
    print(seasons[2])
else:
    print("false entry")

"""

#exercise 2

names = set()

while True:
    user_name = str(input("Enter your name(or press enter to exit): "))
    if user_name == "":
        break

    if user_name in names:
        print("Existing name")
    else:
        names.add(user_name)
        print("New name")


for x in names:
    print(x)

print(names)

#exercise 3


