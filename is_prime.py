def is_prime(num):
  # If num is less than 2 it is not a prime
  if num < 2: 
    return False
  # Largest factor for a num is num / 2
  end = int(num / 2 + 1)
  # from 2 to largest possible factor check if they divide num evenly
  for i in range(2,end):
    if num % i == 0:
      return False
  # if it has no factors it is a prime no
  return True


print(is_prime(19000))
print(is_prime(324))
print(is_prime(5))
print(is_prime(7))
print(is_prime(9))
print(is_prime(11))



