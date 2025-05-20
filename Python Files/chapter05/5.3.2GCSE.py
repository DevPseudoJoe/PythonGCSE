def asknumber(x,y):
  number = int(input(f"Enter a number between {x} and {y}: "))
  while number < x or number > y:
    print("That number is outside ") 
    number = int(input(f"Re-enter a number between {x} and {y}: "))
  return number
    
def calc():
  for x in range (10):
    print((x+1)*number)
    x+=1
    
number = asknumber(1,12)
calc()
