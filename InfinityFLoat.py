

class InfinityFLoat:
    """
    A class for working with decimal numbers of infinite precision.

    This class represents numbers with a base value (`number`) and an
    associated exponent (`exponent_shift`) that scales the base value by
    a power of ten. It enables precise arithmetic and representation of
    numbers in the form `number * 10^(exponent_shift)`.

    Args:
        number         (int): The base integer value of the number.
        exponent_shift (int): The power of 10 by which the base value is scaled.
                              For example, 314 with an exponent_shift of -2
                              represents the number 3.14 (314 * 10^(-2)).
    """
    def __init__(self, number: int, exponent_shift: int):
        self.base_form(number, exponent_shift)
    
    def base_form(self, number: int, exponent_shift: int) -> None:
        while number % 10 == 0:
            number //= 10
            exponent_shift += 1
        self.number = number
        self.exp = exponent_shift
    
    def add(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        min_exp = min(self.exp, other.exp)
        self.set_exponent(min_exp)
        other.set_exponent(min_exp)

        integral_part = self.number + other.number
        return InfinityFLoat(integral_part, min_exp)

    def sub(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    def mul(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    def div(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    
    # helper funcions __________________________________________________________________________
    def digit_count(self, number: int) -> int:
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count
    
    def set_exponent(self, exp: int) -> None:
        dif = self.exp - exp
        self.exp = exp
        self.number *= 10**dif
    
    # magic methonds ___________________________________________________________________________
    def __str__(self):
        if self.exp >= 0:
            return f'{self.number} * 10^{self.exp} => {self.number * 10**(self.exp)}'
        
        exp = -self.exp
        integral_part = self.number // (10**exp)
        decimal_part = self.number - (integral_part * (10**exp))
        zeros = "0"*(exp - self.digit_count(decimal_part))

        return f'{self.number} * 10^{self.exp} => {integral_part},{zeros}{decimal_part}'


fl = InfinityFLoat(5, -2)
print(fl)
fl = InfinityFLoat(5, -1)
print(fl)
fl = InfinityFLoat(5, 0)
print(fl)
fl = InfinityFLoat(123456, -3)
print(fl)
fl = InfinityFLoat(123000456, -3)
print(fl)
fl = InfinityFLoat(123000456, -6)
print(fl)
fl = InfinityFLoat(123000456, -4)
print(fl)

print("__add testing__")

small = InfinityFLoat(5, -2)
big = InfinityFLoat(3, 2)

another = small.add(big)
print(another)

small = InfinityFLoat(5, 5)
big = InfinityFLoat(123456, 10)

another = small.add(big)
print(another)
