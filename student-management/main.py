#main
from student import Student, MasterStudent

name=input("Enter your name:").lower()
department=input("Enter your department:").lower()
section=input("Please select your student type: Bachelor or Master?:").lower()

if section=="master":
    thesis=input("Enter your thesis subject:").lower()
    student= MasterStudent(name,department,thesis)
else:
    student= Student(name,department)

while True:
    print("\n1. Add grade")
    print("2.Show information")
    print("3.Exit")

    choice=input("Choose:  ")
    
    if choice=="1":
        grade=int(input("Enter a grade:"))
        student.add_grade(grade)
    elif choice=="2":
        print(student.information())
    elif choice=="3":
        print("Program finished")
        break
    else:
        print("Invalid choice")