# What’s OOP?
# Imagine everything as objects — a car 🚗, a book 📚, or even a cute little puppy 🐶. OOP helps us model complex systems by treating real-world entities as objects within the program. We assign them classes (their blueprint), attributes (their characteristics), and methods (their actions)!
#
# Key Concepts:
#
# Class: The blueprint or prototype, like a recipe 🍲! Defines the structure for creating objects.
# Object: A specific instance of a class. Think of it as a cake made from that recipe 🎂.
# Attributes: Characteristics or properties of an object, like the color of a car.
# Methods: Actions or behaviors that the object can perform (e.g., drive() for a car).
#
# Example: Create Your First Class!
#Defining the class
class Car:
    color = "green"
    #method
    def drive(self):
        print("Driving")
# Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()

#Example2
class Person:
    favorite_fruit = "Orange"
    def fruit(self):
        print("Fruit are healthy")

person = Person()
print(person.favorite_fruit)
person.fruit()

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
vehicle1 = Vehicle("toyota", "corolla", 2022)
vehicle2 = Vehicle("Ford", "Mustang", 2021)
vehicle3 = Vehicle("Volvo", "Volkswagen", 2011)
print(vehicle1.make, vehicle1.model, vehicle1.year)
print(vehicle2.make, vehicle2.model, vehicle2.year)
print(vehicle3.make, vehicle3.model, vehicle3.year)


