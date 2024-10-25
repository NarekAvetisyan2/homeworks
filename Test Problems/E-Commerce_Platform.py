from abc import ABC, abstractmethod


class Products:
    def __init__(self, name, price, description):
        self.name = name
        self.price =price
        self.description = description

class Customers:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Orders:
    def __init__(self, ord_customer):
        self.ord_customer = ord_customer
        self.ord_prod = []
        self.ord_price = 0
        self.products = []

    def Search_Prod(self, product):
        if product in self.products:
            return self.ord_prod.append(product)
        return "Product not found"

    def Order_Price(self, value, product):
        if product in self.ord_prod:
           return value
        self.ord_price = value


    def Ord_Info(self):
        return f"Total price of orders: {self.ord_price}"


class Prod_Type(ABC):
    @abstractmethod
    def Info_Order(self):
        pass

class Electronics(Prod_Type):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def Info_Order(self):
        return f"{self.name} texnikayi gin@ arji {self.price}$"

class Clothing(Prod_Type):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def Info_Order(self):
        return f"{self.name} hagusti gin@ arji {self.price}$"

electronic = Electronics("Sony", "1500")
print(electronic.Info_Order())
clothing = Clothing("Vernashapik", "99")
print(clothing.Info_Order())
order = Orders("Misak")
order.Search_Prod("Naski")
order.Order_Price("24$", "Naski")
print(order.Ord_Info())

