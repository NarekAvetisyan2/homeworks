class RangeDescriptor:
    def __set__(self, instance, value: int):
        if not isinstance(value, int):
            raise ValueError("Value must be intager")
        if  not 1 < value <100:
            raise ValueError("Value must be in range 1-100")
        instance.Value = value

    def __get__(self, instance, owner):
        return instance.Value

class Price:
    any_price = RangeDescriptor()

price = Price()
price.any_price = 50
print(price.any_price)