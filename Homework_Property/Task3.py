class Temperature:
    def __init__(self, graduse):
        self._Graduse = graduse


    @property
    def Fahrenheit(self):
        return (self._Graduse * 9/5) +32

    @Fahrenheit.setter
    def Fahrenheit(self, value):
        if not isinstance(value,(int, float)):
            raise TypeError("Value must be intager or float")
        self._Graduse = value


c = Temperature(100)
c.Fahrenheit = 60
print(c.Fahrenheit)