class Employ:
    def __init__(self, employ_id, name, salary):
        self.__employ_id = employ_id
        self.__name = name
        self.__salary = salary

    def getEmploy_id(self):
        return self.__employ_id

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def setSalary(self, value):
        if value < 0:
            raise ValueError("Can't be negative value")
        self.salary = value



Person = Employ(123456, "Movses", 54534)

print(Person.getEmploy_id())
print(Person.getName())
print(Person.getSalary())
Person.setSalary(546546)
