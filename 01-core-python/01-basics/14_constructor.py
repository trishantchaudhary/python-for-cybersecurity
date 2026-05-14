# Constructors are special methods used to initialize objects when they are created from a class
# creation and initialization are handled through the __new__() and __init__() methods
# Constructors help assign initial values to object attributes and prepare objects for use


# __init__ function

# invokes at object creation means execute at object creation



class Student:
    # Constructor (__init__)
    def __init__(self, name, age):
        self.name = name  
        self.age = age  

    # Ek simple method 
    def show_info(self):
        print(f"Naam: {self.name}, Umar: {self.age}")


# --- lets create obj---
# when this line will execute , __init__ automatically call ho jayega
student1 = Student("Rahul", 20)

# for output call function
student1.show_info()


# type of constructors
# default constructor doesnt tak any parameter other than self

class Car:
    def __init__(self):

        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

car = Car()
print(car)
print(car.make)
print(car.model)
print(car.year)


# If no constructor is defined in a class, Python automatically provides a default 
# constructor that creates the object without initializing custom attributes.

#Parameterized Constructor: accepts arguments to initialize the 
# object's attributes with specific values.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)


# using self as Defautl arguement
# when defining methods inside a class, first parameter is always self


class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model

# Create an instance of Car
car1 = Car("Toyota", "Corolla")

# Call the display method
print(car1.display())


# The main reason Python uses self is to make object-oriented programming explicit rather than implicit.
#  By requiring the instance of the class as the first parameter,