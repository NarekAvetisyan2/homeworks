from abc import ABC, abstractmethod

class MenuItem:
    __slots__ = ['name', 'price', 'ingredients']

    def __init__(self, name: str, price: int, ingredient: str):
        self.name = name
        self.price = price
        self.ingredients = ingredient

    def getName(self):
        return self.name

    def setName(self, value):
        if value == '':
            raise ValueError("Name must be valid")
        self.name = value

    def getPrice(self):
        return self.price

    def setPrice(self, item_value):
        if item_value < 0:
            raise ValueError("Price must be positive")
        self.price = item_value

    def getIngredients(self):
        return self.ingredients

    def setIngredients(self, components):
        if components == '':
            raise ValueError("")
        self.ingredients = components

class Appetizer(MenuItem):
    __slots__ = ['snacks']

    def __init__(self, name, price, ingredients, snacks: str):
        super().__init__(name, price, ingredients)
        self.snacks = snacks

    def getPickled_Snacks(self):
        return self.snacks

class Entree(MenuItem):
    __slots__ = ['dish']

    def __init__(self, name, price, ingredients, dish):
        super().__init__(name, price, ingredients)
        self.dish = dish

    def getDish(self):
        return self.dish

class Dessert(MenuItem):
    __slots__ = ['fruits']

    def __init__(self, name, price, ingredients, fruits):
        super().__init__(name, price, ingredients)
        self.fruits = fruits

    def getFruits(self):
        return self.fruits

class Customer:
    __slots__ = ['name', 'contact_info', 'order_history']

    def __init__(self, name: str, contact_info: str, order_history):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def getName(self):
        return self.name

    def setName(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        self.name = name

    def getContanct_Info(self):
        return self.contact_info

    def setContact_Info(self, value):
        if value == '':
            raise ValueError("Contact info can't be empty")
        self.contact_info = value

    def Place_Order(self, order):
        return self.order_history.append(order)

    def View_Order_Info(self):
        return self.order_history

class Order(ABC):
    __slots__ = ['customer', 'menu_items', 'total_price']

    def __init__(self, customer, menu_items, total_price):
        self.customer = customer
        self.menu_items = []
        self.total_price = 0

    @abstractmethod
    def Calc_Price(self, price, items):
        self.price = price
        self.item = items

    def Total_Price(self, total_price):
        self.total_price += (self.item * self.price)


if __name__ == "main":
    orde = Order(12, 20)
    print(orde.Total_Price(12))