# Write a method even_nums(max) that takes in a number max and 
# returns an array containing all even numbers from 0 to max

def even_nums(max):
  result = []
  i = 2
  while(i <= max):
    result.append(i)
    i += 2

  return result

print(even_nums(10))

print(even_nums(40))