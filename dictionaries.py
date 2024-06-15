# Accessing values in a dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points}!")

# Adding New Key-Value Pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25 #add that value by brackets
print(alien_0)

# Starting with an empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values in a dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0 = {'color': 'yellow'}
print(f"The alien color is now {alien_0['color']}")

alien_0['speed'] = 'medium'
print(alien_0)

# Removing key value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Dictionary of similar objects & breaking larger dictionaries up

favorite_languages = {
    'trae': 'python',
    'marq': 'java',
    'zach': 'python',
    'hari': 'bash'
}

language = favorite_languages['hari'].title()
print(f"Hari's favorite language is {language}.")
print(favorite_languages['hari'])

# Using get() method to access values

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['speed'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Personal lab 6-1: Person

person = {'first_name': 'trae', 'age': 28, 'city': 'jersey'}

print(person['first_name'])
print(person['age'])
print(person['city'])

favorite_numbers = {'trae': 7, 'marq': 5, 'zach': 2, 'hari': 1}


print(favorite_numbers.items())

# Loopong through a dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

for name, language in favorite_languages.items():
    print(f"\nName: {name}")
    print(f"\nLanguage: {language}")

# to show dictionary in full sentence

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys

for name in favorite_languages.keys():
    print(name.title())

friends = ['trae', 'hari', 'zach', 'marq']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}.")
    
# looping through keys in a particular order

for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.") #alphabetical order

# Looping through all the values

favorite_languages = {
    'trae': 'python',
    'marq': 'java',
    'zach': 'python',
    'hari': 'bash'
}

print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())

"""using the set() function to find unique non repeated items withn a dictionary,
which have repeated items within it"""

print("The following languages have been mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())

# Nesting: storing multiple dictionaries in a list or list of items as a value

alien_0 = {'color': ' green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red','points': 15 }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# using the range function to generate huge lists

for alien_number in range(30):
    new_alien = {'color': ' green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"\nThe total numbers of aliens: {len(aliens)}")

#using for loops to modify the data and change the aliens' color

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] == 10
        print(aliens)

# A list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\n{topping}")

# Nesting a list inside a dictionary

favorite_languages = {
    'trae': ['python', 'bash'],
    'marq': ['java'],
    'zach': ['python', 'rust'],
    'hari': ['bash', 'c#']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite laguages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A dictionary within a dictionary

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title}")