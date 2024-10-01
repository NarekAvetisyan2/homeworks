class Employee:
    def __set__(self, instance, value: int):
        max_salary = 15000
        if not isinstance(value, int):
            raise TypeError("Value must be intager")
        if value < 0 or value > max_salary:
            raise ValueError("Value can't be negative or greater then max salary")
        instance.Salary = value

    def __get__(self, instance, owner):
        return instance.Salary

class UserSalary:
    User = Employee()

user = UserSalary()
user.User = 1200
print(user.User)
