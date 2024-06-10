#Sorting a list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#Printing a List in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Finding the Length of a List (within the terminal)
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

#Personal lab: Vacation places

vacay_places = ['jamaica', 'puerto rico', 'bora bora', 'fiji']
print(vacay_places)

vacay_places.sort()
print(vacay_places)

print("Here is the original list")
print(vacay_places)

vacay_places.sort(reverse=True)
print(vacay_places)

vacay_places.reverse()
print(vacay_places)