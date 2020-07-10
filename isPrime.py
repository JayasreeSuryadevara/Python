def isPrime(num):
  if num < 2: 
    return False
  for i in range(3,num):
    if num % i == 0:
      return False
  return True


print(isPrime(19))
print(isPrime(324))
print(isPrime(5))
print(isPrime(7))
print(isPrime(9))
print(isPrime(11))
