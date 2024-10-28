from module9 import Car

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
        print(f"\nPublication name is : {self.name}, name of the author is {author} and the page count is {page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
        print(f"Publication name is: {self.name}, name of the chief editor is {chief_editor}")

book = Book("Donald duck", "Rosa Liksam" , 192)
magazine = Magazine("Donald Duck" , "Aki Hyppa")



class Electric(Car):
    def __init__(self, regi_num, max_speed, capacity):
        super().__init__(regi_num, max_speed)
        self.capacity = capacity
        print(f"\n Electric car {regi_num} has {max_speed}km/h and has {capacity} kwh capacity")


class Gasoline(Car):
    def __init__(self, regi_num, max_speed, litres):
        super().__init__(regi_num, max_speed)
        self.litres = litres
        print(f"Gasoline car {regi_num} has {max_speed}km/h and has {litres} litres in the tank")

electric = Electric("ABC-15", 180, 52.5)
gasoline = Gasoline("ABC-123", 165, 32.3)

electric.accelerate(100)
electric.drive(3)

gasoline.accelerate(90)
gasoline.drive(3)

print(electric)
print(gasoline)