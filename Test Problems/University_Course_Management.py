from abc import ABC, abstractmethod

class Courses:
    def __init__(self, name, instructor, content):
        self.name = name
        self.instructor = instructor
        self.content = content

class Students:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.course = []
        self.assignments = []
        
    def Info_Student(self) :
        return f"Student: {self.name} , {self.contact_info}"

    def Enroll_Courses(self, new_course):
        return  self.course.append(new_course)

    def View_Courses(self):
        return (f"Course is: {self.course}\n"
                f"Students : ({self.Info_Student()})")

    def Assignments(self, exercises):
        return self.assignments.append(exercises)

    def Assing_Info(self):
        return f"Ended exercises: {self.assignments}"

class Professors:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.courses = []


    def Add_Courses(self, info_student):
        return self.courses.append(info_student)

    def Show_Courses(self):
        return (f"Course :{self.courses}\n"
                f"Professor: {self.name}, {self.contact_info}\n")



kurs = Professors("Math", "Armenak")
kurs.Add_Courses("Mukuch")
kurs.Add_Courses("Misak")
kurs.Add_Courses("Manushak")
print(kurs.Show_Courses())
stud = Students("Mukuch", 123456)
stud = Students("Misak", 234567)
stud.Enroll_Courses("Mathematic")
print(stud.View_Courses())
print(stud.Info_Student())
stud.Assignments("Task1")
stud.Assignments("Task2")
print(stud.Assing_Info())
