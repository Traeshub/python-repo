cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Inequality

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numerical Comparisons

answer = 17
if answer != 42:
    print("That is not a correct answer. Please try again!")

# Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Personal labs 5-1: Conditional tests

car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

car = 'lamborghini'
print("\nIs car == 'lamborghini'? I predict true")
print(car == 'lamborghini')

print("\nIs car == 'ferrari'? I predict false")
print(car == 'ferrari')

if car == 'lamborghini':
    print(car)

if car != 'ferrari':
     print("The car is not a lambo!") #testing inequality

if car != car.lower():
    print(car)
else:
    print("No, this a a rarri!") #testing the lower method

# IF STATEMENTS:

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet!?")

# If Else statements

age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are not old enough to vote.")
    print("Please register to vote when you turn 18!")

# If-elif-Else chain

age = 12
if age < 4:
    print("Your admission costs $0.")
elif age < 18:
    print("Your admission costs $25.")
else:
    print("Your admission costs $40.")

if age < 4: #set the value of the price within the if-elif-else chain instead of printing in each block
    price = 0
elif age < 18:
    price = 25
else:
    price =40
print(f"Your admission cost is ${price}")

# Mulitple Elif blocks

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")

# Omitting the else block

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:      #extra elif block instead of else, allows for more accuracy in some cases.
    price = 20
print(f"Your admission cost is ${price}")