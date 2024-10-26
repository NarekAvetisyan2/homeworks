from abc import ABC, abstractmethod
from functools import total_ordering


class Menu:
    def __init__(self, dishes, price):
        self.dishes = dishes
        self.price = price

class Dishes_Type(ABC):
    @abstractmethod
    def Info_Order(self):
        pass

class Appetizers(Dishes_Type):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def Info_Order(self):
        return f"The cost of one serving {self.name}: {self.price} dram"

class Entrees(Dishes_Type):
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def Info_Order(self):
        return f"The cost of one serving {self.name} is: {self.price} dram"

class Order:
    def __init__(self, customer_ordering, ordered_dishes, total_price):
        self.customer = customer_ordering
        self.total_price = total_price
        self.ordered_dishes = ordered_dishes

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.ordered = []
        self.order_price = 0

    def Ordering(self, entrees, value: int):
        if not entrees in self.ordered:
             self.ordered.append(entrees)
             self.order_price = self.order_price + value
        return f"{self.ordered}, {self.order_price}"


    def Order_Info(self):
        return f"{self.ordered} and total price is {self.order_price}"


# dishes = Entrees("Tolma", "4800")
# print(dishes.Info_Order())
# dishes = Appetizers("Zeytun", "900")
# print(dishes.Info_Order())
customer = Customer("Bob", 123456)
customer.Ordering("Tolma", 100)
print(customer.Order_Info())

