# Write a Python program fizzbuzz(max) which takes an argument max. 
# For multiples of three print "Fizz" instead of the number and 
# for the multiples of five print "Buzz". For numbers 
# which are multiples of both three and five print "FizzBuzz".
def fizzbuzz(max):
  strings = ""
  for num in range(1, max):
    if num % 3 == 0 and num % 5 == 0:
      strings += "FizzBuzz  "
    elif num % 3 == 0:
      strings += "Fizz  "
    elif num % 5 == 0:
      strings += "Buzz  "
  return strings

print(fizzbuzz(24))

