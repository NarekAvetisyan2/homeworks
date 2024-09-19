class Student:
    def __init__(self, name, roll_number, grades):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []

    def Add_Grades(self, grade):
        if grade > 0 and grade < 100:
            self.__grades.append(grade)

    def Calculate_Grades(self):
        return sum(self.__grades) / len(self.__grades)

    def Student_Info(self):
        print(f"Student name: {self.__name}")
        print(f"Roll number: {self.__roll_number}")
        print(f"Grade: {self.__grades}")

New_Student = Student("Poxosa", 45, 4)
New_Student.Student_Info()
