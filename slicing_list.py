# Slicing a list with the range() function

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #this is where the list actually got copied

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('canoli')
friend_foods.append('ice cream') #added to the two lists to show they are still separate ofter the copy

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)