requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

# Personal labs 5-3: Alien colors 1

alien_color = 'red'

if alien_color == 'red':
	print("Player just earned 5 points!")

# Alien colors 2

if alien_color == 'yellow':
	print("Player just earned 5 points!")
else:
	print("Player just earned 10 points!")

# Alien colors 3

if alien_color == 'yellow':
	print("Player just earned 5 points!")
elif alien_color == 'red':
	print("Player just earned 15 points!")
else:
	print("Player just earned 10 points!")

# Personal lab 2: Favorite fruits

favorite_fruits = ['mango', 'pineapple', 'strawberry']

if 'mango' in favorite_fruits:
	print("Mangoes are good")
	print(f"\n{favorite_fruits[0].title()} is my favorite fruit of them all!")
if 'pineapple' in favorite_fruits:
	print("\nPineapples are good")
if 'strawberry' in favorite_fruits:
	print("\nStrawberries are good")
print("\nThese are my favorite fruits!")