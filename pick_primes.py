# Write a method pick_primes that takes in an array of numbers and 
# returns a new array containing only the prime numbers.
import isPrime.py as isPrime

def pick_primes(nums):
  result = []
  for num in nums:
    if isPrime(num):
      result.append(num)
  return result

  
