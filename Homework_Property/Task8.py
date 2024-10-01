class PasswordValidator:
    def __set__(self, instance, value: str):
        max_len = 50
        if not isinstance(value, str):
            raise TypeError("Password must be string of numbers")
        if not 0 < len(value) < max_len:
            raise ValueError("Password must be in range 1 - 10")
        instance.Password = value

    def __get__(self, instance, owner):
        return instance.Password

class Account:
    password = PasswordValidator()

pas = Account()
pas.password = "Password is valid"
print(pas.password)