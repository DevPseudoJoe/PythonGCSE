array = [["00","01","02"],["10","11","12"],["20","21","22"]]

x = len(array)
while x > 0:
  print(f"{x} - {array[x-1]}")
  x=x-1
posinarray1 = int(input("What list would you like to select?\n>>>\t"))

y = len(array[posinarray1-1])
while y > 0:
  print(f"{y} - {array[posinarray1-1][y-1]}")
  y=y-1
posinarray2 = int(input("What item in that list would you like to select?\n>>>\t"))

print(f"You selected the list #{posinarray1}, item #{posinarray2}, which is: {array[posinarray1-1][posinarray2-1]}")