from abc import ABC, abstractmethod

class Movies:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Rentals:
    def __init__(self, customer_rent, rent_duration):
        self.customer_rent = customer_rent
        self.rented_movie = []
        self.rent_duration = rent_duration

    def Rented(self, rented, duration):
        if rented in self.rented_movie:
            return rented
        return self.rent_duration

    def Returned(self, movie):
        return self.rented_movie.append(movie)

class Movies_Type(ABC):
    @abstractmethod
    def Movies_Info(self):
        pass

class Drama(Movies_Type):
    def __init__(self, name):
        self.name = name

    def Movies_Info(self):
        return f"Drama movies name is: {self.name}"

class Comedy(Movies_Type):
    def __init__(self, name):
        self.name = name

    def Movies_Info(self):
        return f"Comedy movies name is: {self.name}"

drama = Drama("Giqor")
print(drama.Movies_Info())
comedy = Comedy("Kargin...")
print(comedy.Movies_Info())
rental = Rentals("21", "Today")
rental.Returned("Torik")
rental.Returned("01-99")
rental.Returned("Santa-Barbra")
print(rental.Rented("01-99", "Today"))