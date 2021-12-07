#Read name and mark from STDIN
#Print the grade

name = input("Name: ")
mark = int(input("Mark: "))

if(mark >= 85):
    grade = "HD"
elif(mark >= 75):
    grade = "D"
elif(mark >= 65):
    grade = "C"
elif(mark >= 50):
    grade = "P"
else:
    grade = "Z"

print("Welcome {}, your mark is {} and your grade is {:*^7}".format(name,mark,grade))
