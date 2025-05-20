def write_to_a_file():
  with open("file_handling_rules.txt","w") as newfile:
    newfile.write("File handling rules\nStep 1: open a file object, in the correct mode, and assign it to a variable.\nStep 2: write or append lines to, or read lines from, the file.\nStep 3: remember to close the file!")

def append_to_a_file():
  write_to_a_file()
  with open("file_handling_rules.txt","a") as newfile:
    newfile.write("\n\nFile handling rules\nBy Maxim Tikhonov")

append_to_a_file()
readfile = open("file_handling_rules.txt","r")
print(readfile.read())