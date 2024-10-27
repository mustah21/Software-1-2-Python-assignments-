import random

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Start at the bottom floor

    def go_to_floor(self, floor):
        while floor != self.current_floor:
            if floor > self.current_floor:
                self.floor_up()
            elif floor < self.current_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moving up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moving down to floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_index, destination_floor):
        if 0 <= elevator_index < len(self.elevators):
            print(f"Running elevator {elevator_index + 1} to floor {destination_floor}.")
            self.elevators[elevator_index].go_to_floor(destination_floor)
        else:
            print("Invalid elevator index.")

    def fire_alarm(self):
        print("Fire alarm! Moving all elevators to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


class Car:
    def __init__(self, regi_num, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = regi_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time_hours):
        self.travelled_distance += self.current_speed * time_hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 10)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration Number':<20}{'Current Speed (km/h)':<20}{'Distance Travelled (km)':<20}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<20}{car.current_speed:<20}{car.travelled_distance:<20}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


def main():
    # Create an elevator and test its functionality
    elevator = Elevator(1, 10)
    elevator.go_to_floor(5)  # Move to the 5th floor
    elevator.go_to_floor(1)  # Return to the bottom floor

    # Create a building with elevators
    building = Building(1, 10, 3)
    building.run_elevator(0, 5)  # Use the first elevator to go to the 5th floor
    building.fire_alarm()  # Trigger the fire alarm

    # Create a race
    cars = [Car(f"ABC-{i+1:03d}", random.randint(100, 200)) for i in range(10)]
    race = Race("Grand Demolition Derby", 8000, cars)

    # Simulate the race
    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            print(f"\nAfter {hours_passed} hours:")
            race.print_status()

    print(f"\nRace finished after {hours_passed} hours!")
    race.print_status()


if __name__ == "__main__":
    main()
