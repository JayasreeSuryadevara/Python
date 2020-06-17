# Write a method range(min, max) that takes in two numbers min and max. 
# The method should return an array containing all numbers from min to max inclusive.

def range(min, max):
  result = []
  while(min <= max):
    result.append(min)
    min += 1

  return result

print(range(5,10))

print(range(1,100))