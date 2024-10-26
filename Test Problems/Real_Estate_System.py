from abc import ABC, abstractmethod


class Properties:
    def __init__(self, address, price, features):
        self.address = address
        self.price = price
        self.features = features

class Agents:
    def __init__(self, name , contact):
        self.name = name
        self.contact = contact

class Clients:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Properties_Type(ABC):
    @abstractmethod
    def real_est_oper(self):
        pass

class Residential(Properties_Type):
    def __init__(self, price: int, square: float):
        self.price = price
        self.square = square

    def real_est_oper(self):
        return f"Home square is {self.square} and price is {self.price}$"

class Commercial(Properties_Type):
    def __init__(self, price: int, square: float):
        self.price = price
        self.square = square

    def real_est_oper(self):
        return f"Office square is {self.square} and price is {self.price}$"

residential = Residential(10000, 56.5)
print(residential.real_est_oper())