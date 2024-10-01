class ValidateString:
    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise TypeError("type error")
        if len(value) < 3:
            raise ValueError("value error")
        instance.name = value


    def __get__(self, instance, owner):
        return instance.name

class User:
    username = ValidateString()

us = User()
us.username = "Stacvec URRRA"
print(us.username)