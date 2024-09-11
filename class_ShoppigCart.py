class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_Items(self,item, price):
        if price < 0:
           raise ValueError("Can't be negative")
        items = (item, price)
        self.__items.append(items)
        return self.__items

    def pop_Items(self):
        if self.__items:
            return self.__items.pop()

    def sum_Items(self):
        return len(self.__items)

Shops = ShoppingCart()
Shops.add_Items("spam", 667)
#Shops.pop_Items()
Shops.sum_Items()
print(Shops.add_Items("ham", 45454))
#print(Shops.pop_Items())
print(Shops.sum_Items())


