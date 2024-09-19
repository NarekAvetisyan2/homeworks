from abc import abstractmethod
from optparse import Option
from symtable import Class
from typing import List, Optional
import datetime

class Account:
    def __init__(self, account_number: int, balance: float, account_type: str):
        self._account_number = account_number
        self._balance = balance
        self._account_type = account_type

        @abstractmethod
        def deposit(self, amount: float) -> None:
            ...

        @abstractmethod
        def withdraw(self, amount: float) -> None:
            ...

        @abstractmethod
        def transfer(self, destination: Account, amount: float) -> None:
            ...

        @abstractmethod
        def show_balance(self) -> None:
            ...

        @abstractmethod
        def get_account_type(self) -> str:
            ...

class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, overdraft_limit: float):
        super().__init__(account_number, balance, account_type)
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount) -> None:
        self._balance += amount

    def withdraw(self, amount) -> None:
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Balance is Low")

    def transfer(self, destination: Account, amount: float) -> None:
        if self._balance >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Balance is a Low")

    def show_balance(self) -> None:
        print(f"Balance amount is: {self._balance}")

    def get_account_type(self) -> str:
        return "Chaking"

class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, innterest_rate: float):
        super().__init__(account_number, balance, account_type)
        self._interest_rate = interest_rate

    def deposit(self, amount) -> None:
        self._balance += amount

    def withdraw(self, amount) -> None:
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Balance is Low")

    def transfer(self, destination: Account, amount: float) -> None:
        if self._balance >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Balance is a Low")

    def show_balance(self) -> None:
        print(f"Balance amount is: {self._balance}")

    def get_account_type(self) -> str:
        return "Saveing"

class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, joint_owners: List[str]):
        super().__init__(account_number, balance, account_type)
        self._joint_owners = joint_owners

    def deposit(self, amount) -> None:
        self._balance += amount

    def withdraw(self, amount) -> None:
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Balance is Low")

    def transfer(self, destination: Account, amount: float) -> None:
        if self._balance >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Balance is a Low")

    def show_balance(self) -> None:
        print(f"Balance amount is: {self._balance}")

    def get_account_type(self) -> str:
        return "Genereted"

    def add_owner(self, customer_name: str) -> None:
        self._joint_owners.append(customer_name)

class TransactionManager:
    def log_transaction(self, transaction_type: str, amount: float) ->None:
        pass

    def show_transaction_history(self):
        pass

class Transaction:
    def __init__(self, from_account: Account, to_account: Optional['Account'], amount: float, transction_type: str, timestamp: datetime):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transction_type
        self.timestamp = datetime

    def log(self) -> None:
        print (f"You have a {self.transaction_type} "
               f"from {self.from_account} "
               f"to {self.to_account} "
               f"on ${self.amount} "
               f"at {self.timestamp}")

class Customer:
    def __init__(self, name: str, contact_info: str, accounts: List[Account]):
        self._name = name
        self._contact_info = contact_info
        self._accounts = accounts

    def add_account(self, account: Account) -> None:
        self._accounts.append(account)

    def view_account(self) -> None:
        print(f"{self._contact_info}")

    def view_transaction_history(self):
        print("Your transaction history: ...")


acc = Account(125, 555, 666)
Chek = CheckingAccount(222, 777, 888, 999)
Chek.deposit(111)
Chek.show_balance()
Custom = Customer('Bob', 'Black list', ["Account"])
Custom.add_account(acc)