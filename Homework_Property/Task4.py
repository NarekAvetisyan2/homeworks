class Descriptor:
    def __get__(self, instance, owner):
        return instance.AGS

    def __set__(self, instance, value):
        if not 0 < value < 100:
            raise ValueError(".....")
        instance.AGS = value

class Student:
    score = Descriptor()

attr = Student()
attr.score = 64
print(attr.score)
