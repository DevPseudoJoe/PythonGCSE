number = int(input("Enter a number between 1 and 20: "))
while number < 1 or number > 20:
  print("Outside range")
  number = int(input("Re-enter a number between 1 and 20: "))

print("In range")
