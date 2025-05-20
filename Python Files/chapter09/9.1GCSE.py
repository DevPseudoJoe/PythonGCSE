def write_to_a_file():
  #newfile = open("file_handling_rules.txt","w")
  #(stremlines code)
  with open("file_handling_rules.txt","w") as newfile:
    newfile.write("File handling rules\nStep 1: open a file object, in the correct mode, and assign it to a variable.\nStep 2: write or append lines to, or read lines from, the file.\nStep 3: remember to close the file!")
  #newfile.close()
  #not needed

write_to_a_file()
openfile = open("file_handling_rules.txt","r")
print(openfile.read())