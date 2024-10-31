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


#Task2

class Electric(Car):
    def __init__(self, regi_num, max_speed, capacity):
        super().__init__(regi_num, max_speed)
        self.capacity = capacity

    def print_drive(self):
        print(f"Distance driven by electric car: {self.travelled_distance} km")


class Gasoline(Car):
    def __init__(self, regi_num, max_speed, litres):
        super().__init__(regi_num, max_speed)
        self.litres = litres

    def print_drive(self):
        print(f"Distance driven by gasoline car: {self.travelled_distance} km")


electric = Electric("ABC-15", 180, 52.5)
gasoline = Gasoline("ABC-123", 165, 32.3)

electric.accelerate(100)
electric.drive(3)
electric.print_drive()

gasoline.accelerate(90)
gasoline.drive(3)
gasoline.print_drive()

