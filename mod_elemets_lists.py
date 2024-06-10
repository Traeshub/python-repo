#modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducait'
print(motorcycles)

#Adding elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#Inserting elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
"""start by defining and printing the list motorcycles 1. Then pop a
value from the list, and assign that value to the variable popped_motorcycle.
print the list to show that a value has been removed from the list.
Then we print the popped value to prove that we still have access to the
value that was removed."""

#Popping Items from Any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned}.")

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#You can also use the remove() method to work with a value that’s being removed from a list.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
	
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#Personal lab: Guest List

guest_list = ['hari', 'zach', 'marq']
message = f"This is a formal invitation inviting you, {guest_list[0].title()}, to Tech Thursdays."
print(message)

guest_list = ['hari', 'zach', 'marq']
message = f"This is a formal invitation inviting you, {guest_list[1].title()}, to Tech Thursdays."
print(message)

guest_list = ['hari', 'zach', 'marq']
message = f"This is a formal invitation inviting you, {guest_list[2].title()}, to Tech Thursdays."
print(message)

#Personal lab: Changing Guest List

guest_list = ['hari', 'zach', 'marq']
guest_list[0] = 'trae'
message = f"This is a formal invitation inviting you, {guest_list[0].title()}, to Tech Thursdays."
print(message)

guest_list = ['hari', 'zach', 'marq']
message = f"This is a formal invitation inviting you, {guest_list[1].title()}, to Tech Thursdays."
print(message)

guest_list = ['hari', 'zach', 'marq']
message = f"This is a formal invitation inviting you, {guest_list[2].title()}, to Tech Thursdays."
print(message)
print('Hari cannot make it so he is replaced with Trae')