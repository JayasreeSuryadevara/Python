# Write a method doubler(numbers) that takes an array of numbers and 
# returns a new array where every element of the original array is multiplied by 2.

def doubler(nums):
  result = []
  for num in nums:
    result.append(num * 2)

  return result

print(doubler([1,2,3,4,5]))
# [2, 4, 6, 8, 10]
print(doubler([56,67,34,56,12]))
# [112, 134, 68, 112, 24]
