#Using list comprehension with square numbers

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

#Personal lab 4-3:

numbers = list(range(1, 21)) #using range functionto create the list 1-20
print(numbers)

for number in numbers: #for loop in order to count from 1-20
    print(number)