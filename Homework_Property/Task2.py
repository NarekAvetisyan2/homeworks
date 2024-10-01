from numbers import Real

class Rectangle:
    def __init__(self, width: Real, height: Real):
        self.Width = width
        self.Height = height

    @property
    def Area(self):
        return 2 * (self.Width + self.Height)

    @Area.setter
    def Area(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Value can't be negative")
        self.Width = width
        self.Height = height

    @property
    def Perimeter(self):
        return self.Height * self.Width

    @Perimeter.setter
    def Perimeter(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Value must be positive")
        self.Width = width
        self.Height = height


r = Rectangle(4, 5)
print(r.Area)
print(r.Perimeter)