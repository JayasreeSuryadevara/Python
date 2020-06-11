# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will 
# turn 100 years old.
# call it : age_to.py
# Extras:
#   Add on to the previous program by asking the user for another number 
#   and printing out that many copies of the previous message. 
#   Print out that many copies of the previous message on separate lines. 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
count = int(input("Enter a number: "))

to_hundred = 100 - age
i = 0

while i < count:
  print(name + " you will be 100 in " + str(to_hundred) + " years!" + "\n")
  i += 1