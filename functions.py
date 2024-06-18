def greet_user():
    """Display a simple greeting."""    # docstring, defines what the function does
    print("Hello!")

greet_user()    #needs this at the end or it will not run

# Passing Information to a Function

def greet_user(username):
    """Display a simple greeting."""    # username is the variable being passed, code is expecting a value for this each time it's called
    print(f"Hello, {username.title()}")

greet_user('trae')

# Arguments and Parameters

def display_message():
    """Displays what i'm learning in this chapter"""
    print("I am learning about arguments and parameters.")

display_message()

# Passing Arguments

def describe_pet(animal_type, pet_name): # these are positional arguments, the function has to go in the order the arguments are placed.
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls

def describe_pet(animal_type, pet_name): 
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'poseidon')

# Keyword Arguments

def describe_pet(animal_type, pet_name): 
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')   #keyword agurments, explicitly tell python which value is paired with which parameter

# Default Values

def describe_pet(pet_name, animal_type='dog'): # default value is animale_type=, it has to be placed last in the arguments
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='poseidon')   #all you have to pass is pet_name bv animal_type is defined by default

# Equivalent Function Calls

describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Return Values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('future', 'hendrix') # when calling a function that returns a value, you need a variable to assign it to
print(musician)

# Making an Argument Optional

def get_formatted_name(first_name, last_name, middle_name= ''): #empty string for optional argument has to be last, also in print call as well
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('future', 'hendrix') 
print(musician)

musician = get_formatted_name('future', 'hendrix', 'pluto')
print(musician)

# Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of info about a person."""
    person = {'first': {first_name}, 'last': {last_name}}
    return person
musician = build_person('future', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of info about a person."""
    person = {'first': {first_name}, 'last': {last_name}}
    if age:
        person[age] = age    
    return person

musician = build_person('future', 'hendrix', age=40)
print(musician)

# Using a Function with a while Loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# Passing a List

def greet_users(names):
    """Print a simple greetin greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function

def printed_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to comopleted_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printed_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List

printed_models(unprinted_designs[:], completed_models) # the slice notation ([:]) makes a copy of the list for the function to use, keeping OG for record

""" you should pass the original list to functions unless you have a specific reason to pass a copy. Its more efficient for a function to work with an existing list, because this avoids using the time and memory
needed to make a separate copy."""

# Passing an Arbitrary Number of Arguments

def make_pizza(*toppings): # the asterisk tells python to make a tuple called toppings containing all the values it receives
    """Summarize the pizza we are about to make."""  
    print("\nMaking pizza with the following toppings:") #the arbitrary function must be last in the function definition
    for topping in toppings:
        print(f"- {topping}")

make_pizza('chicken')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton',
                             field='physics')
print(user_profile)

# Storing Your Functions in Modules & importing modules

def make_pizza(size, *toppings):        # creating a module to store your code in 
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#import pizza           this wouldn't be commeneted usually but i did not store a file called pizza.py in order to import

"""To call a function from an imported module, enter the name of the
module you imported, pizza, followed by the name of the function, make
_pizza(), separated by a dot"""

# pizz.make_pizza(16, 'chicken')  |   an example of how to call a function from an imported module

# Importing Specific Functions | Ex: from pizza import make_pizza

# Using as to Give a Function an Alias
"""from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')""" 

# Using as to Give a Module an Alias
"""import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""

#Importing All Functions in a Module

"""from pizza import *  
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')""" #the asterisk calls every function in the module file

# Styling functions

"""Functions should have descriptive names, and these names should use
lowercase letters and underscores. Module names should use these
conventions as well.

Every function should have a comment that explains concisely what
the function does. This comment should appear immediately after the
function definition and use the docstring format."""