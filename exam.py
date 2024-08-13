# Name:  Abdul Razaq
# Father Name: Abdul Ghani
# Factually: Computer Science
# Department: Software Engineer
# Student_24: [2, 19, 30]

# 2. Add a method called greet to the Person class that prints a greeting message including the
# person's name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, My name is {self.name}.")


person1 = Person("Ahmad", 20)
person1.greet()

# 19. Create a class Company with attributes name and employees (a list of Employee objects).
# Provide methods to add and remove employees.


from dataclasses import dataclass, field
import typing


@dataclass
class Company:
    @dataclass
    class Employee:
        name: str
        salary: int

    name: str
    employees: typing.List[Employee] = field(init=False, default=list)

    def __post_init__(self):
        self.employees = []

    def add_imployee(self, name, salary):
        if name and salary:
            employee = self.Employee(name, salary)
            self.employees.append(employee)

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
        else:
            print("Employee not found")


comp = Company("Amazon")
comp.add_imployee("Ahmad", 10000)
comp.add_imployee("Mahmood", 10000)
comp.add_imployee("Ali", 10000)

for emp in comp.employees:
    print(emp.name, emp.salary)


comp.remove_employee("Ali")
print()
for emp in comp.employees:
    print(emp.name, emp.salary)


# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
# should have attributes room_number and is_occupied. Provide methods to book and checkout rooms

from dataclasses import dataclass, field
import typing


@dataclass
class Hotel:
    @dataclass
    class Room:
        room_no: int
        occupied: bool = False

    name: str
    rooms: typing.List[Room] = field(init=False, default=list)

    def __post_init__(self):
        self.rooms = []

    def book_room(self, room_no):
        if room_no:
            for room in self.rooms:
                if room.room_no == room_no and not room.occupied:
                    room.occupied = True
                    print("Room Booked!")
                    return room_no
            else:
                print("Room Does not Exist")
        else:
            print("Please Enter a room Number")

    def checkout(self, room_no):
        if room_no:
            for room in self.rooms:
                if room.room_no == room_no and room.occupied:
                    room.occupied = False
                    print("Room Checked out")
                    return room_no
            else:
                print("Room Does not Exist")
        else:
            print("Please Enter a room Number")

    def add_room(self, room_no):
        if room_no:
            if self.rooms:
                for room in self.rooms:
                    if room.room_no != room_no:
                        self.rooms.append(self.Room(room_no))
                        return room_no
                else:
                    print("Room Already Exists")
            else:
                self.rooms.append(self.Room(room_no))
        else:
            print("Please Enter a Room Number")

    def get_rooms(self):
        return [(room.room_no, room.occupied) for room in self.rooms]


hotel = Hotel("5 Star hotel")
for i in range(101, 111):
    hotel.add_room(i)

print(hotel.get_rooms())

hotel.book_room(101)
hotel.book_room(103)
hotel.book_room(105)
hotel.book_room(107)
hotel.book_room(111)

print(hotel.get_rooms())

hotel.checkout(103)
hotel.checkout(105)
hotel.checkout(106)

print(hotel.get_rooms())


