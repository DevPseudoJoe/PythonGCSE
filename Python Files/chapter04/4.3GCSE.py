def studentName():
    sName = input("What is your name?")
    return sName

def teacherName():
    tName = input("What is your computing teacher's name?")
    return teacherName

def marks():
    marks1 = int(input("What is your first homework's grade (out of 9): ")
    return marks1

    marks2 = int(input("What is your second homework's grade (out of 9): ")
    return marks2

    marks3 = int(input("What is your third homework's grade (out of 9): ")
    return marks3

    average = (marks1+marks2+marks3)/3
    return average

def teacherComment():
    if average >=8:
       print(f"Well done, {sName}, {tName} is very pleased with your effort.")

    elif average >=6 <8:
        middle = print(f"A good effort, {0}. {1} thinks you should check your work carefully.").format(studentName, teacherName)


    else average <=5:
        print(f"{0} this is poor. {1} has asked you to try harder").format(studentName, teacherName)

studentName() = sName
teacherName() = tName
marks() = average
teacherComment(studentName, teacherName, average)

