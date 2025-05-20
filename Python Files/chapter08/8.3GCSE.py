numberlist = []

number = int(input("Please enter a number:\t"))
numberlist.append(number)
while 0 not in numberlist:
#Can be either "while 0 not in numbers:" or "while number != 0:"
  number = int(input("Please enter a number:\t"))
  numberlist.append(number)

numberlist.sort()
print(numberlist)
