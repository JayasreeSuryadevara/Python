# Write a method prime_factors that takes in a number and returns 
# an array containing all of the prime factors of the given number.
def is_prime(num):
  if num < 2:
    return False
  end = int(num / 2 + 1)
  for i in range(2, end):
    if num % i == 0:
      return False
  return True


def prime_factors(num):
  factors = []
  end = int(num / 2 + 1)
  for i in range(2,end):
    if is_prime(i) and num % i == 0:
    # if  num % i == 0:
      factors.append(i)
  return factors


print(prime_factors(222))
print(prime_factors(30))
print(prime_factors(10))
print(prime_factors(10000))


