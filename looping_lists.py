#use a for loop to print out each name in a list of magicians

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#adding a f string to a for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    # \n is to tell the code to go to the next line for the text for readability.

#Summarizing the block of code

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show.\n") #this can be whatever msg

#Personl lab 4-1: Pizzas

pizzas = ['plain', 'margarita', 'buffalo chicken']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza}.\n")

print("I really love pizza!")