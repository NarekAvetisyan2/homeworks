

class Fraction:
    def __init__(self, numerator:int, denominator:int):
        if denominator == 0:
            raise ZeroDivisionError("Denominator can't be 0")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) ->str:
        if self.denominator == 1:
            return (f"{self.numerator}")
        else:
            return(f"{self.numerator/self.denominator}")

    def __repr__(self) ->str:
        return (f"Numerator is: {self.numerator}\n"
                f"Denominator is: {self.denominator}")

    def __add__(self, other: int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid .")
        numerator_add = self.numerator
        denominator_add = self.denominator
        return numerator_add + denominator_add

    def __sub__(self, other: int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid ..")
        numerator_sub = self.numerator
        denominator_sub = self.denominator
        return numerator_sub - denominator_sub

    def __mul__(self, other: int) ->int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid ...")
        numerator_mul = self.numerator
        denominator_mul = self.denominator
        return numerator_mul * denominator_mul

    def __truediv__(self, other: int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid ....")
        if other.denominator == 0:
            raise ZeroDivisionError("Can't be 0...")
        numerator_div = self.numerator
        denominator_div = self.denominator
        return numerator_div / denominator_div

    def __eq__(self, other: int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid")
        numerator_eq = self.numerator
        denominator_eq = self.denominator
        if numerator_eq != denominator_eq:
            raise ValueError("numerator_eq must be equal denominator_eq")
        return  f"{numerator_eq} = {denominator_eq}"

    def __ne__(self, other: int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid")
        numerator_ne = self.numerator
        denominator_ne = self.denominator
        if numerator_ne == denominator_ne:
            raise ValueError("numerator_ne can't be equal denominator_ne")
        return f"{numerator_ne} != {denominator_ne}"

    def __lt__(self, other:int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid")
        numerator_lt = self.numerator
        denominator_lt = self.denominator
        if numerator_lt >= denominator_lt:
            raise ValueError("numerator_lt must be less then denominator_lt")
        return f"{numerator_lt} < {denominator_lt}"

    def __le__(self, other:int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid")
        numerator_le = self.numerator
        denominator_le = self.denominator
        if numerator_le > denominator_le:
            raise ValueError("numerator_le must be equal or less then denominator_le")
        return f"{numerator_le} <= {denominator_le}"

    def __gt__(self, other:int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid")
        numerator_gt = self.numerator
        denominator_gt = self.denominator
        if numerator_gt <= denominator_gt:
            raise ValueError("numerator_gt must be greater then denominator_gt")
        return f"{numerator_gt} > {denominator_gt}"

    def __ge__(self, other:int) -> int:
        if not isinstance(other, Fraction):
            raise NotImplemented("Invalid")
        numerator_ge = self.numerator
        denominator_ge = self.denominator
        if numerator_ge < denominator_ge:
            raise ValueError("numerator_ge must be equal or greater then denominator_ge")
        return f"{numerator_ge} >= {denominator_ge}"

    def __hash__(self) -> int:
        return hash((self.numerator, self.denominator))

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __neg__(self) -> int:
        if self.numerator < 0:
            self.numerator = -self.numerator
        if self.denominator < 0:
            self.denominator = -self.denominator

    # def __iadd__(self, other):
    #     if not isinstance(other, Fraction):
    #         raise NotImplemented("....")
    #     numerator_iadd = self.numerator
    #     denominator_iadd = self.denominator
    #     return self.numerator += self.denominator


if __name__ == "__main__":
    fraction1 = Fraction(5, 5)
    fraction2 = Fraction(4, 8)

    print(fraction1)
    print(fraction2)

    # print(fraction1 + fraction2)
    # print(fraction1 - fraction2)
    # print(fraction1 * fraction2)
    # print(fraction1 / fraction2)
    # print(fraction1 == fraction2)
    # print(fraction1 != fraction2)
    # print(fraction1 < fraction2)
    # print(fraction1 <= fraction2)
    # print(fraction1 > fraction2)
    # print(fraction1 >= fraction2)
    # print(hash(fraction1))
    # print(hash(fraction2))
    # print(hash(fraction1 == fraction2)) # Nuyn@ chi berum
    # print(float(fraction1 / fraction2)) # stexel tarberutyun chi talis tranc divisioni het
    # print(fraction1 += fraction2) # syntax errora talis


