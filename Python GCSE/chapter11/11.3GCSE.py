def writeToFile():
  filename = input("Name your file: ")
  if filename == "main.py":
    print("Please use another name!")
    return writeToFile()
  else:
    with open (filename, "w") as file:
      file.write("hello")
    main()

def main():
  writeToFile = input("Please name the file you want to read: ")
  try:
    with open (writeToFile, "r") as file:
      print(file.read())
  except FileNotFoundError:
    print("That is not a real file")
    return main()

# Call the 'main' func
if __name__ == "__main__":
  writeToFile()