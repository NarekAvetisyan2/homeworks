from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, product_type, model):
        self.product_type = product_type
        self.model = model

    @abstractmethod
    def Prod_Type(self):
        pass

    @abstractmethod
    def Model(self):
        pass

class Customers:
    def __init__(self, name, contact):
        self._name = name
        self._contact = contact

    def Customer_Info(self):
        return (f"Customer name is: {self._name}\n"
              f"Customer contact is: {self._contact}")

class Salespeople(Car):
    def __init__(self, model, product_type, name, target: int, price, commision=0.05):
        super().__init__(model,product_type)
        self.name = name
        # self.commision = 0.5
        self.target = target
        self.price = price


    def Price(self, value):
        if value <= 0:
            raise ValueError("Price can't be negativ or zero")
        self.price = value

    def Model(self):
        return self.model

    def Prod_Type(self):
        return self.product_type

    def Result(self):

        # self.result =
        return (self.target * 0.05 * self.price)

    def Sale_Info(self):
        return (f"From {self.product_type} sale {self.name}'s incom is: {self.Result()}")

    def Customer_Info(self):
        return (f"Customer name is: {self._name}\n"
              f"Customer contact is: {self._contact}")


cust = Customers("Bob",123456)
print(cust.Customer_Info())
salespeople = Salespeople("Tesla", "Electric", "Ani", 5, 10000)
print(salespeople.Sale_Info())

