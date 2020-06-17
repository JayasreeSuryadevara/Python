# function to remove vowels from a given string

def removeVowels(str):
  result = ""
  for char in str:
    if char not in "aeiou":
      result += char

  return result


print(removeVowels("ticecreekcodersrock"))
#  tccrkcdrsrck
print(removeVowels("consectetur adipiscing elit"))
#  cnscttr dpscng lt

print(removeVowels(
    "Florida protester Oluwatoyin Salau, 19, found dead in Tallahassee after going missing"))
