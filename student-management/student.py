#Student Management/Grade System Mini Project

class Person:
    def __init__(self,name):
        self.name=name

    def information(self):
        return self.name
    
class Student(Person):
    def __init__(self,name,department,grades):
        super().__init__(name)
        self.department=department
        self.grades=[]
    
    def add_grade(self,grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades)==0:
            return 0
        return sum(self.grades)/len(self.grades)
        
    def status(self):
        if self.average()>=50:
            return "Passed"
        else:
            return "Failed"
    
    def information(self):
        return self.name, self.department,self.grades,self.average(),self.status()

class MasterStudent(Student):
    def __init__(self,name,department,thesis):
        super().__init__(name,department)
        self.thesis=thesis

    def information(self):
        basis=super().information()
        return basis, self.thesis
    
