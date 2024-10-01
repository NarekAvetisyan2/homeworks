# class Person:
#     def __init__(self, age):
#         self.Age = age
#
#
#     def getAge(self):
#        return self.__age
#
#     def setAge(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("Value can't be float or negativ")
#         self.__age = value
#     Age = property(getAge, setAge)

class Person:
    def __init__(self, age: int):
        self.Age = age

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Value can't be float or negativ")
        self.__age = value

    # Age = property(getAge, setAge)

p = Person(45)
print(p.Age)