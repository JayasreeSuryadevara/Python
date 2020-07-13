# Write a method pick_primes that takes in an array of numbers and 
# returns a new array containing only the prime numbers.
def is_prime(num):
  if num < 2:
    return False
  end = int(num / 2 + 1)
  for i in range(2, end):
    if num % i == 0:
      return False
  return True


def pick_primes(nums):
  result = []
  for num in nums:
    if is_prime(num):
      result.append(num)
  return result


print(pick_primes([12,11,24,35,33,77,55,48,111]))
print(pick_primes([1,2,3,4,5,6,7,8,9,10]))
