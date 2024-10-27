from module9 import Car
import random
import time

#Task 1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor > self.top_floor or floor < self.bottom_floor:
            print("Invalid floor")
            return
        while floor > self.current_floor:
            self.floor_up()
        while floor < self.current_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"You are currently on floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"You are currently on floor: {self.current_floor}")

ele = Elevator(1,9)

ele.go_to_floor(8)
ele.go_to_floor(3)
ele.go_to_floor(15)

#Task 2 and 3
class Building:
    def __init__(self, top_floor, bottom_floor, num):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.num_of_elevators = num
        self.elevators = []
        for i in range(num):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator( self, elev, dest_floor):
        if 0 <= elev < self.num_of_elevators:
            self.elevators[elev].go_to_floor(dest_floor)
            print(f"You are currently on elevator {elev} and your floor is {self.elevators[elev].current_floor}")
        else:
            print("Your entry was invalid")

    def fire_alarm(self):
        for i in self.elevators:
            i.go_to_floor(self.bottom_floor)
            print("All elevators have been moved to the bottom floor")
            #Since in this code only two elevators have been used so they have been moved to the bottom floor.


new = Building(9,1,5)
new.run_elevator(0,6)
new.run_elevator(3,4)
new.fire_alarm()



#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
#The new race is given a list of ten cars similarly to the earlier exercise.
#The main program simulates the progressing of the race by calling the hour_passes in a loop,
#after which it uses the race_finished method to check if the race has finished.
#The current status is printed out using the print_status method every ten hours and then once more at the end of the race.

#This exercise continues the previous car race exercise from the last exercise set.
#Write a Race class that has the following properties:
#name, distance in kilometers and a list of cars participating in the race.
#The class has an initializer that receives the name, kilometers,
# and car list as parameters and sets their values to the corresponding properties in the class.

# The class has the following methods:

#hour_passes, which performs the operations done once per hour in the original exercise:
#generates a random change of speed for each car and calls their drive method.

#print_status, which prints out the current information of each car as a clear, formatted table.

#race_finished, which returns True if any of the cars has reached the finish line,
#meaning that they have driven the entire distance of the race.

#Task 4
class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change  = random.randint(-10,10)
            car.accelerate(speed_change)
            car.drive(1)


    def print_status(self):
        for car in self.cars:
            print(f"{car.registration_number}: Speed = {car.current_speed} km/h, Distance = {car.travelled_distance} km")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance_km for car in self.cars)


cars = [Car(f"ABC-{i+1:03d}", random.randint(100, 200)) for i in range(10)]
race = Race("Grand Demolition Derby", 8000, cars)

hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1

    if hours_passed % 10 == 0:
        race.print_status()

race.print_status()
print(f"Race finished after {hours_passed} hours!")


