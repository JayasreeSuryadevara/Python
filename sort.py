def sort(num1, num2):
  list = []
  if num1 > num2:
    list.append(num1)
    list.append(num2)
  else:
    list.append(num2)
    list.append(num1)
  
  print(list)


sort(455, 677)
sort(3,4)
sort(9,10001)
sort("a","b")