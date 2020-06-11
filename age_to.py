name = input("Enter your name: ")
age = int(input("Enter your age: "))
count = int(input("Enter the no of repeats: "))

to_hundred = 100 - age
i = 1

while i <= count:
  print( name + " you will be 100 in " + str(to_hundred) + " years!")
  print(i)
  i += 1