# Getting the input for x and y
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))

# initialize the lists
xList = []
yList = []
bigList = []

# filling in xList and yList
i = 1
while i <= 10:
  xList.append(x)
  yList.append(y)
  i += 1

# create bigList
bigList = xList + yList

print(xList)
print(yList)
print(bigList)
