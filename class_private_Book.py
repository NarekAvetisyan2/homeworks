class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def setPrice(self, value):
        if value < 10:
            raise ValueError("Price can't be low 10")
        self.__price = value

    def getPrice(self):
        return self.__price

Best_Book = Book("Lav_girq", "Armen", 11)
print(Best_Book.getTitle())
print(Best_Book.getAuthor())
print(Best_Book.getPrice())
print(Best_Book.setPrice(12))