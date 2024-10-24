class Accounts:
    def __init__(self, acc_number, balance, acc_type):
        self._acc_number = acc_number
        self.balance = balance
        self._acc_type = acc_type

class Customers:
    def __init__(self, name, contact):
        self._name = name
        self._contact = contact

    def Customer_Info(self):
        return (f"Customer name is: {self._name}\n"
              f"Customer contact is: {self._contact}")

class CheckAcc(Accounts):
    def __init__(self, acc_number, balance, acc_type, overdraft_limit):
        super().__init__(acc_number,balance,acc_type)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        if self.balance < amount:
            print("No money")
        else:
            self.balance -= amount

    def get_info(self):
        return f"Balance is: {self.balance}"

    def info_acc_type(self):
        return "Chaking"


class SaveAcc(Accounts):
    def __init__(self, acc_number, balance, acc_type, overdraft_limit):
        super().__init__(acc_number, balance, acc_type)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        if self.balance < amount:
            print("No money")
        else:
            self.balance -= amount

    def get_info(self):
        return f"Balance is: {self.balance}"

    def info_acc_type(self):
        return "Saving"

class Transaction:
    def __init__(self, from_acc, to_acc, amount):
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount

    def Transaction_Info(self):
        return (f"{self.from_acc} send {self.amount}$ to {self.to_acc}")


acc = Accounts(123, 1000, "saving")
chek = CheckAcc(100, 1000, "saving", 300)
chek.withdraw(500)
print(chek.get_info())
chek.deposit((1000))
print(chek.get_info())
trans = Transaction("Bob", "Ann", 500)
print(trans.Transaction_Info())
customer = Customers("Ann", 123456)
print(customer.Customer_Info())

