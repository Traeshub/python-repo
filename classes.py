# Object-oriented programming (OOP)
"""In object-oriented programming,
you write classes that represent real-world things
and situations, and you create objects based on these
classes. When you write a class, you define the general
behavior that a whole category of objects can have."""

# Creating and Using a Class

class Dog:   #capitalized names refer to classes
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """initialize name and age attributes."""
        self.name = name    #these are called attributes
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a commnad."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!!")

# Making an Instance from a Class

my_dog = Dog('Poseidon', 1)

print(f"My dog's name is {my_dog.name}.")      # the dot notation is how you access attributes
print(f"My dog is {my_dog.age} years old.")

# Calling Methods

my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances

my_dog = Dog('Poseidon', 1)
your_dog = Dog('King', 2)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"\nYour dog is {your_dog.age} years old.")
your_dog.sit()

# Personal lab 9-1: Restaurant

class Restaurant:
    """Simulate a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
       """initialize restaurant name & cuisine type attributes"""
       self.restaurant_name = restaurant_name
       self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """simulate describing a restaurant."""
        print(f"The name of this restaurant is {self.restaurant_name}.")
        print(f"\nThe cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Telling if the restaurant is open."""
        print(f"\n {self.restaurant_name} is now open.")

restaurant = Restaurant('Chipotle', 'mexican food')

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Working with Classes and Instances

class Car:
    """simple attempt to simulate a car."""
    def __init__(self, make, model, year):
        """initialize attributes describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """return a nearly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('lamborghini', 'revuelto', 2025)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute

class Car:
    """simple attempt to simulate a car."""
    def __init__(self, make, model, year):
        """initialize attributes describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
my_new_car = Car('lamborghini', 'revuelto', 2025)
print(my_new_car)
my_new_car.read_odometer()

# Inheritance

class Car:
    """simple attempt to simulate a car."""
    def __init__(self, make, model, year):
        """initialize attributes describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class ElectricCar(Car): #inheritance class, also can add it's on attributes if needed
    """represents aspects of a car, specific to eletric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('telsa', 'model 3', 2025)
print(my_tesla)

# Defining Attributes and Methods for the Child Class

class ElectricCar(Car): #inheritance class, also can add it's on attributes if needed
    """represents aspects of a car, specific to eletric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 100

    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}--kwh battery.")

my_tesla = ElectricCar('telsa', 'model 3', 2025)
print(my_tesla)     # this line would have .descriptive name but not in this example bc program is broken up
my_tesla.describe_battery()

# Instances as Attributes, also called Composition

class Battery:
    """A simple attempt to model a battery for an electric car."""

def __init__(self, battery_size=40):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size

def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car): #inheritance class, also can add it's on attributes if needed
    """represents aspects of a car, specific to eletric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
Then initialize attributes specific to an electric car."""
        
        super().__init__(make, model, year)
        #self.battery() = Battery()

my_tesla = ElectricCar('telsa', 'model 3', 2025)
print(my_tesla)
my_tesla.battery.describe_battery

# Importing Classes

class Car: # this is an example of the file i would import from
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")

def update_odometer(self, mileage):
    """
Set the odometer reading to the given value.
Reject the change if it attempts to roll the odometer back.
"""
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")

def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

# from car import Car           # only commmented so file could save, other wise it is  not commented, this is where you import.

my_new_car = Car('lamborghini', 'ruvuelto', 2025)
print(my_new_car)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Using Aliases

""" from electric_car import ElectricCar as EC """