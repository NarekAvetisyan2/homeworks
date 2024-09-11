from functools import reduce
from itertools import product


class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def getProduct_id(self):
        return self.__product_id

    def stock(self):
        return self.__quantity_in_stock

    def setProduct_id(self, id):
        self.__product_id = id

    def getProduct_name(self):
        return self.__product_name

    def setProduct_name(self, name):
        self.__product_name = name

    def AddQuantity_in_stock(self, value):
        if value <= 0:
            raise ValueError("The stock is empty")
        self.__quantity_in_stock += value

    def ReduceQuantity_in_stock(self, value):
        if value > self.__quantity_in_stock:
            raise ValueError("The value can't be bigger then stock")
        self.__quantity_in_stock -= value


Prod = Product(45646, 'Clock', 5)
# Prod.getProduct_id()
# Prod.getProduct_name()
Prod.setProduct_name("Mirg")
Prod.AddQuantity_in_stock(2)

print(Prod.getProduct_name())
print(Prod.getProduct_id())
print(Prod.stock())
Prod.ReduceQuantity_in_stock(3)
print(Prod.stock())


