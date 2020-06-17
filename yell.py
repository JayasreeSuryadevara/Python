# Write a method yell(words) that takes in an array of words and 
# returns a new array where every word from the original array 
# has an exclamation point after it.

def yell(words):
  wordsArr = words.split(" ")
  result = []
  for word in wordsArr:
    result.append(word + "!")

  return " ".join(result)


print(yell("Hello world"))

print(yell("I think Python is cool"))

