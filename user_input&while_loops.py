# Using the input function

message = input("Tell me something, and I will repeat it back to you")
print(message)

name = input("Please enter your name:")
#print(f"\nHello, {name}!")

prompt = "If you share your name, we can personlize the messages you see."
prompt += "\nWhat is your first name?" #the += sign adds new string to the end of the first prompt variable

name = input(prompt)
print(f"\nHello {name}")

#Using int() to Accept Numerical Input

age = input("How old are you?")
age = int(age)

height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to get on the ride!")
else:
    print("\nYou'll be able to ride when you get a little older.")

# The Modulo Operator: divides one number by another number and returns the remainder

4 % 3
5 & 3       # the first expresssion returns 1 as a remainder, the second returs 2.

number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# Personal lab: Rental car

car = input("What kind of rental car would you like today?")
print(f"\nLet me see if I can find you a {car}")

guests = input("How many people are in your dinner group?")
guests = int(guests)

if guests > 8:
    print("You'll have to wait until a table is ready")
else:
    print("\nYour table is ready, please follow the waitress")


# WHILE LOOPS

current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

prompt = input("Tell me something, and I will repeat it back to you:")
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message) # this if statement is there to fix the program needing the user to type quit in quotations.

# Using a flag

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        break
    else:
        print(message)

# Using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a loop

current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number) # the program "continued" past the even numbers, the if statement identifies that

# Personal labs: Pizza toppings

prompt = input("Enter the pizza toppings you would like:")
prompt += "\nEnter quit when you're done choosing."

while True:
    pizza_toppings = input(prompt)

    if pizza_toppings == 'quit':
        break
    else:
        print(f"\nWe're adding {pizza_toppings}!")

# Using a while Loop with Lists and Dictionaries

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # verifies and moves each user until there is none left in the list

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input

responses = {}
polling_active = True #setting a flag to notify that the progrma is active

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response #storing the response in a dictionary

    repeat = input("Would you like another person to respond? (yes/no)")    #repeatint the input for additional data
    if repeat == 'no':
        polling_active = False

print(("\n---Poll Results ---"))
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Personal labs: Deli

sandwich_orders = ['chicken parm', 'turkey', 'pb&j']
finished_sanwiches = []

for sandwich_order in sandwich_orders:
    print(f"\nYour {sandwich_order} is being made.")
else:
    print(f"\nEach samdwich was made!")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sanwiches.append(current_sandwich)

print(finished_sanwiches) #print to show that the list moved from sandqich_orders to finished_sanwiches