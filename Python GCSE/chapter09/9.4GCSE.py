def gettestscore():
title = input("What is the book title?\n\t>>> ")
year = input("What year did the book come out?\n\t>>> ")

def librarycode(title, year):
  parta = title[0:3].upper()
  partb = year[2:4]
  bookcode = parta+partb
  return bookcode
  
def writefile():
  bookcode = librarycode(title, year)
  with open("bookcodes.txt","w") as book:
    book.write(bookcode)
writefile()
