from dataclasses import dataclass, field
import math
from abc import ABC, abstractmethod
import datetime
import json
from turtle import left
from venv import create
import mysql.connector
import typing
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import sqlite3
import requests

# class Sqlite3Connection:
#     def __init__(self, db_name):
#         self.db_name = db_name

#     class Table:
#         def __init__(self, table_name):
#             self.table_name = table_name
#             self.columns = []

#         def add_column(self, column_name, column_type):
#             self.columns.append((column_name, column_type))

#         def generate_create_table_sql(self):
#             columns_sql = ", ".join([f"{name} {type}" for name, type in self.columns])
#             return f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns_sql});"

#     def create_table(self, table):
#         create_table_sql = table.generate_create_table_sql()
#         try:
#             conn = sqlite3.connect(self.db_name)
#             c = conn.cursor()
#             c.execute(create_table_sql)
#             conn.commit()
#             conn.close()
#             print(f"Table {table.table_name} created successfully")
#         except sqlite3.Error as e:
#             print(e)

#     def insert_values(self, insert_sql, values):
#         try:
#             conn = sqlite3.connect(self.db_name)
#             c = conn.cursor()
#             c.execute(insert_sql, values)
#             conn.commit()
#             conn.close()
#             print("Values inserted successfully")
#         except sqlite3.Error as e:
#             print(e)

#     def update_values(self, update_sql, values):
#         try:
#             conn = sqlite3.connect(self.db_name)
#             c = conn.cursor()
#             c.execute(update_sql, values)
#             conn.commit()
#             conn.close()
#             print("Values updated successfully")
#         except sqlite3.Error as e:
#             print(e)

#     def delete_values(self, delete_sql, values):
#         try:
#             conn = sqlite3.connect(self.db_name)
#             c = conn.cursor()
#             c.execute(delete_sql, values)
#             conn.commit()
#             conn.close()
#             print("Values deleted successfully")
#         except sqlite3.Error as e:
#             print(e)

#     def retrieve_columns(self, select_sql):
#         try:
#             conn = sqlite3.connect(self.db_name)
#             c = conn.cursor()
#             c.execute(select_sql)
#             columns = c.fetchall()
#             conn.close()
#             return columns
#         except sqlite3.Error as e:
#             print(e)
#             return None


# Basic Class and Object Exercises
# 1. Create a class called Person with attributes name and age. Create an object of the class and print its attributes.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"My name is {self.name}, and I am {self.age} years old."

# person = Person("Ahmad", 20)
# print(person)

# 2. Add a method called greet to the Person class that prints a greeting message including the person's name.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"My name is {self.name}, and I am {self.age} years old."

#     def greet(self):
#         print(f"Hello, My name is {self.name}.")

# person = Person("Ahmad", 20)
# person.greet()

# 3. Create a class called Car with attributes make, model, and year. Include a method to print out the car's details.


# @dataclass
# class Car:
#     make:str
#     model:str
#     year:int

# car = Car("Toyota", "Corolla", "2020")
# print(car)

# 4. Create a class Circle with a method to compute the area. Initialize the class with the radius.

# @dataclass
# class Circle:
#     radius:float

#     def area(self):
#         return math.pi * (self.radius**2)

# circle = Circle(7)
# print(circle.area())

# 5. Create a class Rectangle with methods to compute the area and perimeter. Initialize the class with the length
# and width.

# @dataclass
# class Rectangle:
#     width:int
#     height:int

#     @property
#     def area(self):
#         return self.width * self.height

#     @property
#     def perimeter(self):
#         return 2* (self.width + self.height)

# rect = Rectangle(7,3)
# print(rect.area, rect.perimeter)

# Inheritance and Polymorphism Exercises
# 6. Create a base class Animal with a method speak. Create two derived
# classes Dog and Cat that override the speak method.

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         print("Animal")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")
#     pass

# class Cat(Animal):
#     def speak(self):
#         print("Meow")

# cat = Cat()
# cat.speak()
# dog = Dog()
# dog.speak()

# 7. Create a base class Shape with a method area. Create derived classes Square and Triangle that implement the area
# method.

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def area(self, side):
#         return side**2

# class Triangle(Shape):
#     def area(self, width, height):
#         return (width*height)/2

# sqr = Square()
# print(sqr.area(10))

# tri = Triangle()
# print(tri.area(10,12))

# 8. Create a class Employee with attributes name and salary. Create a derived class Manager with an additional
# attribute department.

# @dataclass
# class Employee:
#     name:str
#     salary:float


# @dataclass
# class Manager(Employee):
#     department:str

# 9. Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that override the drive
# method.

# class Vehicle(ABC):

#     @abstractmethod
#     def drive():
#         pass

# class Bike(Vehicle):

#     @staticmethod
#     def drive():
#         print("Bike moves")

# class Truck(Vehicle):

#     @staticmethod
#     def drive():
#         print("Truck moves")


# bike = Bike()
# bike.drive()
# truck = Truck()
# truck.drive()

# 10. Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override the fly method
# in Penguin to indicate that penguins cannot fly.

# class Bird(ABC):

#     @abstractmethod
#     def fly():
#         pass

# class Eagle(Vehicle):

#     @staticmethod
#     def fly():
#         print("Eagle can fly!")

# class Penguin(Vehicle):

#     @staticmethod
#     def fly():
#         print("Penguin can not fly")


# Encapsulation and Abstraction Exercises
# 11. Create a class Account with private attributes balance. Provide public methods to deposit and withdraw money.

# class Account:
#     def __init__(self, balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return f"Your balance is {self._balance}."

#     def deposit(self, amount):
#         self._balance += amount
#         print(f"You deposited {amount}.")
#         print(self.balance)

#     def withdraw(self, amount):
#         self._balance -= amount
#         print(f"You withdrew {amount}.")
#         print(self.balance)

# account = Account(1000)
# account.deposit(100)
# account.withdraw(200)`

# 12. Create a class Book with private attributes title, author, and pages. Provide public methods to get and set
# these attributes.

# class Book:
#     def __init__(self, title, author, pages):
#         self._title = title
#         self._author = author
#         self._pages = pages

#     @property
#     def title(self):
#         return f"The title of the book is {self._title}"

#     @title.setter
#     def title(self, title):
#         self._title = title

#     @property
#     def author(self):
#         return f"The author of the book is {self._author}"

#     @author.setter
#     def author(self, author):
#         self._author = author

#     @property
#     def pages(self):
#         return f"The book has {self._pages} pages."

#     @pages.setter
#     def pages(self, pages):
#         self._pages = pages


# book = Book("OOPs", "EMF", 10)

# 13. Create a class Laptop with private attributes brand, model, and price. Provide a method to apply a discount
# and a method to display laptop details.

# @dataclass
# class Laptop:
#     _brand:str
#     _model:str
#     _price:float

#     @property
#     def brand(self):
#         return self._brand

#     @brand.setter
#     def brand(self, brand):
#         self._brand = brand

#     @property
#     def model(self):
#         return self._model

#     @model.setter
#     def model(self, model):
#         self._model = model

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, price):
#         self._price = price

#     def give_discount(self, amount):
#         print(self.price*(1-amount))


# laptop = Laptop("Dell", "7400", 18000)
# print(laptop)
# laptop.give_discount(0.1)

# 14. Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit,
# withdraw, and check the balance.

# @dataclass
# class BankAccount:
#     _account_number:int
#     _balance:int

#     @property
#     def account_number(self):
#         return self._account_number

#     @account_number.setter
#     def account_number(self, account_number):
#         self._account_number = account_number

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self,balance):
#         self._balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"You deposited {amount} of cash.")
#         print(self)

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"You withdrew {amount} of cash.")
#         print(self)

# account1 = BankAccount(1232143, 1000)

# 15. Create a class Student with private attributes name, grade, and age. Provide methods to get and set these
# attributes and a method to display the student's details.

# @dataclass
# class Student:
#     _name:str
#     _grade:str
#     _age:int

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         self._name = name

#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age


# Class Relationships and Advanced Concepts Exercises
# 16. Create a class Library with attributes name and books (a list of Book objects). Provide methods to add and
# remove books.

# @dataclass
# class Library:
#     @dataclass
#     class Book:
#         title: str
#         author: str
#
#     _name: str
#     _books: typing.List
#
#     @property
#     def name(self):
#         return self.name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     @property
#     def books(self):
#         return ", ".join(self._books)
#
#     @books.setter
#     def books(self, books):
#         self._books = books
#
#     def __iadd__(self, book):
#         self._books.append(book)
#         print(f"{book} added to the books list.")
#         return self

# 17. Create a class School with attributes name and students (a list of Student objects). Provide methods to add and
# remove students.

# @dataclass
# class School:
#     @dataclass
#     class Student:
#         _name: str
#         _age: int
#         _grade: str
#
#     _name: str
#     _students: list
#
#
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def __eq__(self, other):
#         if self.name == other.name and self.age == other.age and self.grade == other.grade:
#             return True
#         return False
#
#     def __repr__(self):
#         return f"School.Student(name='{self.name}', age={self.age}, grade='{self.grade}')"

# 18. Create a class Team with attributes name and members (a list of Person objects). Provide methods to add and
# remove members.

# @dataclass
# class Team:
#     @dataclass
#     class Person:
#         _name:str
#         _age:int

#     _name:str
#     _members:list
#     @property
#     def members(self):
#         return self._members
#     def add_members(self, member):
#         self.members.append(member)
#         print(f"{member} added to members list.")

#     def remove_members(self, member):
#         for i in self.members:
#             if i == member:
#                 self.members.remove(i)
#                 print(f"{member} removed from members list.")

# 19. Create a class Company with attributes name and employees (a list of Employee objects). Provide methods to add
# and remove employees.

# @dataclass
# class Company:
#     @dataclass
#     class Employee:
#         _name: str
#         _salary: int
#         _department: str
#
#     _name: str
#     _employees: list
#
#     @property
#     def employees(self):
#         return self._employees
#
#     def __iadd__(self, employee):
#         for emp in self.employees:
#             if emp == employee:
#                 print(f"{employee} already exists.")
#                 break
#         else:
#             self.employees.append(employee)
#         return self
#
#     def __isub__(self, employee):
#         for emp in self.employees:
#             if emp == employee:
#                 self.employees.remove(emp)
#                 break
#         else:
#             print(f"{employee} not found")
#         return self


# 20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods to add and
# remove animals.
#
# @dataclass
# class Zoo:
#     @dataclass
#     class Animal:
#         _type: str
#         _sex: str
#         _number: int
#
#     _name: str
#     _animals: list
#
#     @property
#     def animals(self):
#         return self._animals
#
#     def add_animal(self, animal):
#         for anm in self.animals:
#             if animal == anm:
#                 print(f"{anm} already exists")
#                 break
#         else:
#             self.animals.append(animal)
#
#     def remove_animal(self, animal):
#         for anm in self.animals:
#             if animal == anm:
#                 self.animals.remove(animal)
#                 print(f"{anm} removed.")
#                 break
#         else:
#             print(f"{animal} does not exist.")

# File Handling and Exceptions Exercises
# 21. Create a class FileManager with methods to read from and write to a file.

# class FileManager:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def write_to_file(self, content):
#         try:
#             with open(self.file_path, "w") as file:
#                 file.write(content)
#             print(f"Successfully wrote to {self.file_path}")
#
#         except Exception as e:
#             print(f"An Error Occurred as {e}")
#
#     def append_to_file(self, content):
#         try:
#             with open(self.file_path) as file:
#                 file.write(content)
#             print(f"Successfully wrote to {self.file_path}")
#         except Exception as e:
#             print(f"An error occurred while appending to the file: {e}")
#
#     def read_from_file(self):
#         try:
#             with open(self.file_path) as file:
#                 return file.read()
#         except FileNotFoundError:
#             print(f"File {self.file_path} not found")
#             return None
#
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")
#             return None

# 22. Create a class Log with methods to write error messages to a log file.

# class Log:
#     def __init__(self, log_file):
#         self.log_file = log_file
#
#     def get_timestamp(self):
#         return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#     def write_error(self, message):
#         try:
#             with open(self.log_file, "a") as file:
#                 timestamp = self.get_timestamp()
#                 log_entry = f"[Error] {timestamp} - {message}\n"
#                 file.write(log_entry)
#
#         except Exception as e:
#             print(f"An error occurred while handling the log file {self.log_file}: {e}")


# 23. Create a class Config that reads configuration settings from a file and provides methods to access these settings.


# class Config:
#     def __init__(self, config_file):
#         self.config_file = config_file
#         self.settings = self._read_config()
#
#     def _read_config(self):
#         """Read the configuration file and return the settings as a dictionary."""
#         try:
#             with open(self.config_file, 'r') as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             print(f"Configuration file {self.config_file} not found.")
#             return {}
#         except json.JSONDecodeError:
#             print(f"Error decoding JSON from the configuration file {self.config_file}.")
#             return {}
#
#     def get(self, key, default=None):
#         """Get a configuration value by key."""
#         keys = key.split('.')
#         value = self.settings
#         try:
#             for k in keys:
#                 value = value[k]
#             return value
#         except KeyError:
#             return default


# 24. Create a class Database that connects to a database and provides methods to execute queries. Handle exceptions
# if the connection fails.

# @dataclass
# class DatabaseConnection:
#     host: str
#     port: int
#     username: str
#     password: str
#     database_name: str
#     connection: mysql.connector.connection.MySQLConnectionAbstract = field(init=False, default=None)
#
#     def __post_init__(self):
#         self.connection = self.connect()
#
#     def connect(self):
#         try:
#             connection = mysql.connector.connect(
#                 user=self.username,
#                 password=self.password,
#                 host=self.host,
#                 database=self.database_name,
#                 port=self.port
#             )
#             print("Connection Successful!")
#             return connection
#
#         except mysql.connector.Error as e:
#             print(f"An Error occurred while connecting to the database: {e}")
#
#         except Exception as e:
#             print(f"An Unknown Error occurred while connecting to the database: {e}")
#
#     def close_connection(self):
#         if self.connection:
#             self.connection.close()
#             print("Connection Closed")
#         else:
#             print("You haven't Initialized a connection")
#
#     def execute_command(self, command):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(command)
#             if command.strip().upper().startswith("SELECT") or command.strip().upper().startswith("SHOW"):
#                 for i in cursor:
#                     print(i)
#             print(f"Executed command: {command}")
#         except mysql.connector.Error as e:
#             print(f"An Error occurred while executing the command {command} : {e}")
#
#         finally:
#             cursor.close()
#
#
# db_connection = DatabaseConnection(
#     host="localhost",
#     port=3306,
#     username="root",
#     password="",
#     database_name='test'
# )
#
# db_connection.execute_command("SHOW TABLES;")
# print(db_connection)

# 25. Create a class Report that generates a report from data in a file. Provide methods to handle exceptions if the
# file does not exist or cannot be read.

# class Report:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def generate_report(self):
#         try:
#             with open(self.filename, "r") as file:
#                 data = file.read()
#                 # Generate report from data
#
#                 print(data)
#         except FileNotFoundError:
#             print(f"File {self.filename} not found!")
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")

# Real-world Application Exercises
# 26. Create a class Ticket for a movie theater with attributes movie_name,
# seat_number, and price. Provide methods to display ticket details and apply discounts.

# @dataclass
# class Ticket:
#     movie_name:str
#     seat_name:str
#     price:int
#
#     def give_discount(self, amount):
#         return self.price * (1-amount)

# 27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should be an object of a
# class Item with attributes name and price.


# @dataclass
# class ShoppingCart:
#     @dataclass
#     class Item:
#         name: str
#         price: int
#
#     items: list = field(init=False)
#
#     def __post_init__(self):
#         self.items = []
#
#     def add(self, item_name, price):
#         item = self.Item(item_name, price)
#         for itm in self.items:
#             if itm == item:
#                 print(f"Item {item.name} already added to the cart")
#                 break
#         else:
#             self.items.append(item)
#
#     def remove(self, item_name):
#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(f"Item {item_name} removed from the cart.")
#                 break
#         else:
#             print(f"Item {item_name} not available in the cart.")
#
#
#     def __str__(self):
#         if not self.items:
#             print("Shopping cart is empty")
#         else:
#             string = "\n".join(f"{item.name}: {item.price}" for item in self.items)
#             return f"Items in the Shopping cart:\n{string}"


# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide methods to add and
# remove items from the menu.

# @dataclass
# class Restaurant:
#     @dataclass
#     class Item:
#         name: str
#         price: int
#
#     name: str
#     menu_items: typing.List[Item] = field(default_factory=list)
#
#     def add_item(self, item_name: str, price: int):
#         item = self.Item(item_name, price)
#         for itm in self.menu_items:
#             if itm == item:
#                 print(f"Item already added to the menu!")
#                 break
#         else:
#             self.menu_items.append(item)
#             print(f"Item {item.name} added to the menu.")
#
#     def remove_item(self, item_name: str):
#         for item in self.menu_items:
#             if item.name == item_name:
#                 self.menu_items.remove(item)
#                 print(f"Item {item_name} removed from menu")
#                 break
#         else:
#             print(f"Item {item_name} not found in menu!")
#
#     def __str__(self):
#         if not self.menu_items:
#             print("Menu is empty")
#             return None
#         items = "\n".join(f"{item.name}: {item.price}" for item in self.menu_items)
#         return f"Items Menu\n{items}"


# 29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person objects).
# Provide methods to add and remove passengers.
#
# @dataclass
# class Flight:
#     @dataclass
#     class Passenger:
#         name: str
#         age: int
#         passport_no: str
#
#     flight_number: int
#     destination: str
#     passengers: typing.List[Passenger] = field(default_factory=list)
#
#     def add_passenger(self, passenger_name, passenger_age, passenger_passport):
#         passenger = self.Passenger(passenger_name, passenger_age, passenger_passport)
#         for item in self.passengers:
#             if item == passenger:
#                 print(f"Passenger {passenger_name} already added.")
#                 break
#         else:
#             self.passengers.append(passenger)
#             print(f"Passenger {passenger_name} added to the list.")
#
#     def remove_passenger(self, passenger_name, passenger_passport):
#         for item in self.passengers:
#             if item.name == passenger_name and item.passport_no == passenger_passport:
#                 self.passengers.remove(item)
#                 print(f"Passenger {passenger_name} removed from the list.")
#                 break
#         else:
#             print(f"Passenger {passenger_name} does not exist.")


# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room should have attributes
# room_number and is_occupied. Provide methods to book and check-out rooms.


# @dataclass
# class Hotel:
#     @dataclass
#     class Room:
#         room_number: int
#         is_occupied: bool = False

#     name: str
#     rooms: typing.Set[Room] = field(default_factory=set)

#     def add_room(self, room_number):
#         room = self.Room(room_number)
#         for item in self.rooms:
#             if item.room_number == room_number:
#                 print(f"Room {room_number} already exists.")
#                 break
#         else:
#             self.rooms.add(room)
#             print(f"Room {room_number} added to the list")

#     def book_room(self, room_number, booked_by):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 if room.is_occupied:
#                     print(f"Room {room_number} is already occupied.")
#                 else:
#                     room.is_occupied = True
#                     room.booked_by = booked_by
#                     print(f"Room {room_number} was booked by {booked_by}.")
#                 return
#         else:
#             print(f"Room {room_number} does not exist!")

#     def check_out(self, room_number):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 if room.is_occupied:
#                     print(f"Room {room_number} was checked-out.")
#                     room.is_occupied = False
#                     room.booked_by = ""  # Clear booked_by when checking out
#                 else:
#                     print(f"The room {room_number} was not booked.")
#                 return
#         else:
#             print(f"Room {room_number} does not exist!")


# GUI Application Exercises
# 31. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and decrement buttons.

# class CounterApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")
#         self.root.title("Counter App")
#         self.root.minsize(300, 200)

#         self.label = tk.Label(self.root, text="0", font=("Arial", 32))
#         self.label.pack(pady = (50,0))

#         self.button_frame = tk.Frame(self.root)
#         self.button_frame.pack(pady = 10)

#         self.next_button = tk.Button(self.button_frame, text="Next", font=("Arial", 12), width=10, command=lambda:self.button_action(1))
#         self.prev_button = tk.Button(self.button_frame, text="Previous", font=("Arial", 12), width=10, command=lambda:self.button_action(-1))

#         self.next_button.grid(row=0, column=1)
#         self.prev_button.grid(row=0, column=0)

#         self.root.mainloop()

#     def button_action(self, value):
#         self.label.config(text=f"{int(self.label['text'])+value}")

# 32. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and remove tasks.


# class ToDoApp:
#     @dataclass
#     class LabelManager:
#         content: str
#         parent: typing.Optional[tk.Widget] = None
#         label: tk.Label = field(init=False)
#
#         def __post_init__(self):
#             self.label = tk.Label(self.parent, text=self.content, font=("Arial", 16))
#
#     def __init__(self):
#         self.main_menu = None
#         self.frame = None
#         self.root = tk.Tk()
#         self.root.geometry("600x400")
#         self.root.title("ToDo App")
#         self.root.minsize(600, 400)
#         self.labels = []
#         self.tk_labels = []
#
#         self.create_menubar()
#         self.title = tk.Label(self.root, text="To Do list", font=("Arial", 20))
#         self.title.pack(pady=10)
#         self.create_frames()
#         self.display_labels()
#         self.root.mainloop()
#
#     def create_menubar(self):
#         self.main_menu = tk.Menu(self.root)
#
#         self.action_menu = tk.Menu(self.main_menu, tearoff=0)
#         self.main_menu.add_cascade(label="Action", menu=self.action_menu)
#
#         self.action_menu.add_command(label="Add", command=self.add_label)
#         self.action_menu.add_command(label="Remove", command=self.remove_label)
#         self.action_menu.add_command(label="Edit", command=self.edit_label)
#
#         self.root.config(menu=self.main_menu)
#
#     def create_frames(self):
#         self.frame = tk.Frame(self.root)
#         self.frame.pack(fill='both', expand=True)
#
#     def display_labels(self):
#         if self.labels or self.tk_labels:
#             for label in self.tk_labels:
#                 label.destroy()
#             self.tk_labels.clear()
#             for index, label in enumerate(self.labels):
#                 self.tk_labels.append(tk.Label(self.frame, text=f"{index + 1}- {label.content}", font=("Arial", 12)))
#             for label in self.tk_labels:
#                 label.pack(pady=(0, 10), padx=(20), anchor="w")
#
#     def create_window(self, button_content, function):
#         window = tk.Toplevel(self.root)
#         window.geometry("400x100")
#
#         frame = tk.Frame(window)
#         frame.pack(padx=20, pady=10)
#
#         label = tk.Label(frame, text="Content: ", font=("Arial", 12))
#         label.grid(row=0, column=0, padx=(0, 10))
#
#         entry = tk.Entry(frame, width=50, font=("Arial", 12))
#         entry.grid(row=0, column=1)
#
#         button = tk.Button(window, text=button_content, font=("Arial", 12), command=function)
#         button.pack(pady=10)
#
#         return window, entry
#
#     def add_label(self):
#         def create_label():
#             if entry.get():
#                 label_obj = self.LabelManager(entry.get(), self.frame)
#                 self.labels.append(label_obj)
#                 self.display_labels()
#                 window.destroy()
#             else:
#                 messagebox.showinfo(title="Empty box!", message="You didn't fill the input box!")
#                 window.destroy()
#
#         window, entry = self.create_window("Add", create_label)
#
#     def remove_label(self):
#         def remove():
#             if selection_box.get()[:2].isdigit():
#                 label_number = int(selection_box.get()[:2])
#             else:
#                 label_number = int(selection_box.get()[:1])
#
#             del self.labels[label_number - 1]
#             self.display_labels()
#             options_window.destroy()
#             messagebox.showinfo(title="Remove Content!", message="Content was successfully deleted.")
#
#         if self.labels:
#             options = [
#                 f"{index + 1}- {value.content if len(value.content) <= 10 else value.content[:9]}{'...' if len(value.content) > 10 else ''}"
#                 for index, value in enumerate(self.labels)]
#
#             options_window = tk.Toplevel(self.root)
#             options_window.geometry("400x100")
#
#             selection_box = ttk.Combobox(options_window, values=options, state='readonly')
#             selection_box.set(options[0])
#             selection_box.pack(pady=10)
#
#             button = tk.Button(options_window, text="Select", font=("Arial", 12), command=remove)
#             button.pack(pady=10)
#
#         else:
#             messagebox.showwarning("Empty", "No content inserted")
#
#     def edit_label(self):
#         def edit_label():
#             def create_label():
#                 options_window.destroy()
#                 if entry.get():
#                     self.labels[label_number - 1].content = entry.get()
#                     self.display_labels()
#                     messagebox.showinfo(title="Content Edit!", message="Content was successfully edited.")
#                     window.destroy()
#                 else:
#                     messagebox.showinfo(title="Empty box!", message="You didn't fill the input box!")
#                     window.destroy()
#
#             if selection_box.get()[:2].isdigit():
#                 label_number = int(selection_box.get()[:2])
#             else:
#                 label_number = int(selection_box.get()[:1])
#             window, entry = self.create_window("Edit", create_label)
#             entry.insert(0, self.labels[label_number - 1].content)
#
#         if self.labels:
#
#             options = [
#                 f"{index + 1}- {value.content if len(value.content) <= 10 else value.content[:9]}{'...' if len(value.content) > 10 else ''}"
#                 for index, value in enumerate(self.labels)]
#
#             options_window = tk.Toplevel(self.root)
#             options_window.geometry("400x100")
#
#             selection_box = ttk.Combobox(options_window, values=options, state='readonly')
#             selection_box.set(options[0])
#             selection_box.pack(pady=10)
#
#             button = tk.Button(options_window, text="Select", font=("Arial", 12), command=edit_label)
#             button.pack(pady=10)
#
#         else:
#             messagebox.showwarning("Empty", "No content inserted")
#

# 33. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.

# class CalculatorApp:
#     @dataclass(repr=False, eq=False)
#     class TkButton:
#         value: str
#         parent: typing.Optional[tk.Widget]
#         entry_value: typing.Optional[tk.Variable]
#         row: int
#         column: int
#         columnspan: int = 1
#         command_type: bool = False
#
#         # Class variable to indicate if the equation is solved
#         solved: bool = False
#
#         def __post_init__(self):
#
#             self.display_button()
#             self.signs = ['+', "-", "x", "/"]
#
#         def display_button(self):
#             button = tk.Button(self.parent, text=self.value, font=("Arial", 16), command=self.button_action)
#             button.grid(row=self.row, column=self.column, columnspan=self.columnspan, sticky='ewns', padx=2, pady=2)
#
#         def button_action(self):
#             if not self.command_type:
#                 if CalculatorApp.TkButton.solved:
#                     CalculatorApp.TkButton.solved = False
#                     self.entry_value.set("")
#                 return self.insert()
#             else:
#                 if self.value in ["C", "CE"]:
#                     self.entry_value.set("")
#                     CalculatorApp.TkButton.solved = False
#                     return
#                 if self.value == "=":
#                     if self.entry_value.get():
#                         try:
#                             equation = self.entry_value.get()
#                             equation = equation.replace("x", "*")
#                             if equation[0] == "0" and equation[1] in map(str, range(0, 10)):
#                                 equation = equation[1:]
#                                 self.entry_value.set(equation)
#                                 return self.button_action()
#                             if equation[-1] in self.signs:
#                                 equation = equation[:-1]
#                                 self.entry_value.set(equation)
#                                 return self.button_action()
#                             if equation == ".":
#                                 equation = equation[:-1]
#                                 self.entry_value.set(equation)
#                                 return self.button_action()
#
#                             CalculatorApp.TkButton.solved = True
#                             self.entry_value.set(eval(equation))
#                             return
#
#                         except Exception as e:
#                             self.entry_value.set("")
#                             messagebox.showerror("Error", f"{e}")
#                             return
#
#                     else:
#                         return
#
#                 if self.value == ".":
#                     equation: str = self.entry_value.get()
#                     last_index = 0
#                     for sign in self.signs:
#                         for index, value in enumerate(equation):
#                             if value == sign:
#                                 if index and index > last_index:
#                                     last_index = index
#                     for i in equation[last_index:]:
#                         if i == ".":
#                             break
#                     else:
#                         self.insert()
#
#                 if self.value in self.signs:
#                     entry = self.entry_value.get()
#                     if entry:
#                         if entry[-1] in self.signs:
#                             pass
#                         else:
#                             self.insert()
#                     else:
#                         if self.value in ["+", "-"]:
#                             self.insert()
#
#                 if self.value == "CE":
#                     self.entry_value.set("")
#                     return
#
#                 if self.value == "C":
#                     self.entry_value.set(self.entry_value.get()[:-1])
#                     return
#
#         def insert(self):
#             entry_data = self.entry_value.get() + self.value
#             self.entry_value.set(entry_data)
#
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("400x300")
#         self.root.minsize(300, 200)
#         self.root.title("Calculator")
#         self.root.resizable(width=False, height=False)
#
#         self.equation = tk.StringVar()
#         self.equation.set('')
#         self.entry = tk.Entry(self.root, font=("Arial", 20), state="readonly", textvariable=self.equation)
#         self.entry.pack(padx=10, pady=10, fill='x')
#
#         self.frame = tk.Frame(self.root)
#         self.frame.pack(fill='both', expand=True)
#         for i in range(4):
#             self.frame.grid_rowconfigure(i, weight=1)
#             self.frame.grid_columnconfigure(i, weight=1)
#         self.frame.grid_rowconfigure(4, weight=1)
#
#         self.buttons = []
#         self.create_buttons()
#
#         self.root.mainloop()
#
#     def create_buttons(self):
#         self.buttons.append(self.TkButton("+", self.frame, self.equation, 0, 0, 2, command_type=True))
#         self.buttons.append(self.TkButton("-", self.frame, self.equation, 0, 2, 2, command_type=True))
#         self.buttons.append(self.TkButton("x", self.frame, self.equation, 1, 3, 1, command_type=True))
#         self.buttons.append(self.TkButton("/", self.frame, self.equation, 2, 3, 1, command_type=True))
#         self.buttons.append(self.TkButton(".", self.frame, self.equation, 3, 3, 1, command_type=True))
#         self.buttons.append(self.TkButton("=", self.frame, self.equation, 4, 3, 1, command_type=True))
#         self.buttons.append(self.TkButton("CE", self.frame, self.equation, 4, 2, 1, command_type=True))
#         self.buttons.append(self.TkButton("C", self.frame, self.equation, 4, 0, 1, command_type=True))
#         self.buttons.append(self.TkButton("0", self.frame, self.equation, 4, 1, 1))
#
#         row = 0
#         for i in range(9):
#             if i % 3 == 0:
#                 row += 1
#             self.buttons.append(self.TkButton(f"{i + 1}", self.frame, self.equation, row, i - (row - 1) * 3))
#
#
# CalculatorApp()
#

# 34. Create a class LoginApp that uses tkinter to create a login form GUI.

# class LoginApp:
#     @dataclass
#     class User:
#         __username: str
#         __password: str
#
#         @property
#         def username(self):
#             return self.__username
#
#         @username.setter
#         def username(self, username):
#             self.__username = username
#
#         @property
#         def password(self):
#             return self.__password
#
#         @password.setter
#         def password(self, password):
#             self.__password = password
#
#     def __init__(self, username, password):
#         self.root = tk.Tk()
#         self.root.geometry("600x400")
#         self.root.title("Login App")
#         self.root.resizable(width=False, height=False)
#
#         self.root.grid_rowconfigure(0, weight=1)
#         self.root.grid_columnconfigure(0, weight=1)
#         self.frame = tk.Frame(self.root)
#         self.frame.grid(row=0, column=0)
#
#         self.username_input = tk.StringVar()
#         self.username_label = tk.Label(self.frame, text="Username: ", font=("Arial", 14))
#         self.username_entry = tk.Entry(self.frame, font=("Arial", 14), textvariable=self.username_input)
#
#         self.password_input = tk.StringVar()
#         self.password_label = tk.Label(self.frame, text="Password: ", font=("Arial", 14))
#         self.password_entry = tk.Entry(self.frame, font=("Arial", 14), textvariable=self.password_input)
#
#         self.username_label.grid(row=0, column=0, pady=(0, 40), padx=(0, 20))
#         self.username_entry.grid(row=0, column=1, pady=(0, 40))
#
#         self.password_label.grid(row=1, column=0, pady=(0, 40), padx=(0, 20))
#         self.password_entry.grid(row=1, column=1, pady=(0, 40))
#
#         self.submit_button = tk.Button(self.frame, text="Submit", font=("Arial", 12), command=self.on_submit, width=10)
#         self.submit_button.grid(row=3, column=0, columnspan=2)
#
#         self.user = self.User(username, password)
#
#         self.username_entry.bind("<Return>", self.on_submit)
#         self.password_entry.bind("<Return>", self.on_submit)
#
#         self.root.mainloop()
#
#     def on_submit(self, event=None):
#         if self.username_input.get() and self.password_input.get():
#             if self.username_input.get() == self.user.username and self.password_input.get() == self.user.password:
#                 messagebox.showinfo("Successful", "You logged in successfully")
#                 self.root.destroy()
#             else:
#                 messagebox.showerror("Wrong Credentials", "Username or Password incorrect!")
#                 self.username_input.set("")
#                 self.password_input.set("")
#         else:
#             messagebox.showwarning("Empty Entry", "Please fill the Entry boxes")
#
#
# LoginApp("ali", "123")

# 35. Create a class WeatherApp that uses tkinter to create a weather information GUI.


# class WeatherApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Weather App")
#
#         self.api_key = "369d67c1c7a74a4689f163211242307"
#         self.base_url = "http://api.weatherapi.com/v1/current.json"
#
#         self.city_label = tk.Label(root, text="City:")
#         self.city_label.pack(pady=5)
#
#         self.city_entry = tk.Entry(root)
#         self.city_entry.pack(pady=5)
#
#         self.fetch_button = tk.Button(root, text="Get Weather", command=self.get_weather)
#         self.fetch_button.pack(pady=10)
#
#         self.weather_info = tk.Text(root, height=10, width=50)
#         self.weather_info.pack(pady=5)
#
#     def get_weather(self):
#         city = self.city_entry.get()
#         if city:
#             weather_data = self.fetch_weather_data(city)
#             if weather_data:
#                 self.display_weather(weather_data)
#             else:
#                 messagebox.showerror("API Error", "Could not fetch weather data.")
#         else:
#             messagebox.showwarning("Input Error", "Please enter a city name.")
#
#     def fetch_weather_data(self, city):
#         try:
#             params = {
#                 'key': self.api_key,
#                 'q': city
#             }
#             response = requests.get(self.base_url, params=params)
#             response.raise_for_status()
#
#             data = response.json()
#
#             for i in data:
#                 print(data[i])
#             weather_info = f"Weather data for {city}:\n"
#             weather_info += f"Temperature: {data['current']['temp_c']}°C\n"
#             weather_info += f"Condition: {data['current']['condition']['text']}\n"
#             weather_info += f"Humidity: {data['current']['humidity']}%\n"
#             weather_info += f"Wind: {data['current']['wind_kph']} km/h"
#             return weather_info
#         except requests.RequestException as e:
#             print(f"Error fetching data: {e}")
#             return None
#
#     def display_weather(self, weather_data):
#         self.weather_info.delete(1.0, tk.END)
#
#         self.weather_info.insert(tk.END, weather_data)
#
#
# root = tk.Tk()
# app = WeatherApp(root)
#
# root.mainloop()
