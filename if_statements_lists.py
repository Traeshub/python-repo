# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese',]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#if an items changes during the for loop

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

    print("\nFinished making your pizza!")

# Checking That a List Is Not Empty

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese',]

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want plain pizza?")

# Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"\nSorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#Personal labs 5-8: Hello Admin

usernames = ['admin', 'hari', 'zach', 'marq', 'trae']

for username in usernames:
    if username == 'admin':
        print("\nHello Admin, would you like to see a status report?")
    elif usernames == []:
        print("\nWe need to find some users!!!")
    else:
        print(f"\nHello {username}, thank you for logging in again.")

# No users
usernames = []

if usernames == []:
        print("\nWe need to find some users!!!") # added the 'elif' to the previous code block to intergarate no user check.


# Checking usernames

usernames = ['admin', 'hari', 'zach', 'marq', 'trae']

new_users = ['admin', 'vic', 'ted', 'cam', 'trae']

for new_user in new_users:
    if new_user in usernames:
        print("\nThis username is already used.")
    else:
        print("\nThis username is available.")