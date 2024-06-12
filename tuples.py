dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple

for dimension in dimensions:
    print(dimension)

#Writing Over a Tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

    # Personla lab 4-13: Buffet

    foods = ('tacos', 'pizza', 'chicken', 'wings', 'pasta')
    for food in foods:
        print(food)

    #foods[1] = 'cake' #python rejected the attempted tuple change

    print("Here's the original food menu")
    print(foods)
    
    foods = ('tacos', 'pasta', 'pizza', 'cake', 'chicken')
    print("\nModified food menu")
    print(foods)