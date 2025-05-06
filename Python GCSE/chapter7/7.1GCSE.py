def convert():
  kilometers = int(input("Please enter the number of kilometers:\t"))
  conversion_factor = 1.61
  miles = (f"{kilometers} is {kilometers*conversion_factor:.2f} miles")
  return miles

miles = convert()
print(miles)
