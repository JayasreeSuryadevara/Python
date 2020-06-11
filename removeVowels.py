# function to remove vowels from a given string

def removeVowels(str):
  result = ""
  for char in str:
    if char not in "aeiou":
      result += char

  return result


print(removeVowels("leetcodeisacommunityforcoders"))
