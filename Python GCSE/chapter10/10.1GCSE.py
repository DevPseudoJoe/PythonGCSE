def getTestScore():
  while True:
    testPercentage = input("What test percentage did you get?\n>>> ")
    if testPercentage.isdigit():
      testPercentage = int(testPercentage)
      if testPercentage in range(0, 101):
        print("That is a valid test score.")
        return testPercentage
      else:
        print("That is not a valid test score!")
        return getTestScore()
    else:
      print("That is not a valid test score!")
      return getTestScore()

def main():
  testPercentage = getTestScore()
  if testPercentage >= 90:
    print("You got a 9")
  elif testPercentage >= 80:
    print("You got an 8")
  elif testPercentage >= 70:
    print("you got a 7")
  elif testPercentage >= 60:
    print("you got a 6")
  elif testPercentage < 60:
    print("You failed")
  else:
    print("error occured")


if __name__ == "__main__":
  main()