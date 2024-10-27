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
        print(f"\n After {hours_passed} hours")
        race.print_status()


race.print_status()
print(f"Race finished after {hours_passed} hours!")


