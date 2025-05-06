def CreateStudentFile():
  with open("students.txt","w") as students:
    students.write("Adrian\nCharlie\nRobin\nAlbert\nLucas\nAlex\nMaximK\nGeorge\nAndy\nFilip\nMichael\nMaximT\nJoe\n")

def Main():
  CreateStudentFile()
  with open("students.txt","r") as studentsfile:
    studentlist = studentsfile.readlines()
    studentlist.sort()
  for each in studentlist:
    print(each.strip())
    

Main()