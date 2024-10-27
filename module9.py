import random


class Car:
    def __init__(self, regi_num, max_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = regi_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_speed):
        self.current_speed = self.current_speed + change_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time_hours):
        self.travelled_distance += self.current_speed * time_hours

#TASK 1
car1 = Car('ABC-123', 142)
print(f"""Registration number: {car1.registration_number}, Maximum speed: {car1.max_speed}""")

#Task 2
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)
print(f"Current speed: {car1.current_speed}")

#Task 3
car1.accelerate(100)            #To show the function works fine
car1.drive(1.5)
print(f"Travelled distance: {car1.travelled_distance}")

#Task 4

cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i+1), random.randint(100,200)))

distance_max = 0
while distance_max < 10000:
    for car in cars:
        speed_change = random.randint(-10,15)
        car.accelerate(speed_change)
        car.drive(1)
        distance_max = max(distance_max, car.travelled_distance)

for car in cars:
    print(f"Registration number: {car.registration_number}:, Current speed: {car.current_speed}km/h, Final distance: {car.travelled_distance}")

car = Car('ABC-123', 142)
print(f"\nTesting one car:")
print(f"Registration number: {car.registration_number}:")
print(f"Maximum speed: {car.max_speed}:")
print(f"Current speed: {car.current_speed}")
print(f"Travelled distance: {car.travelled_distance}")
