
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
        sign           (int): -1 or 1
        digit_count    (int): digit count of number
        digit_limit    (int): limit of digits (precission)
    """
    def __init__(self, number=0, exponent_shift=0, digit_limit=1000):
        self.set(number, exponent_shift)
        self.digit_limit = digit_limit

    def set(self, number: int, exponent_shift: int) -> None:
        self.base_form(number, exponent_shift)

    def base_form(self, number: int, exponent_shift: int) -> None:
        self.sign = 1 if number >= 0 else -1
        num = abs(number)
        while num % 10 == 0 and num > 0:
            num //= 10
            exponent_shift += 1
        self.number = num
        self.exp = exponent_shift
        self.digit_count = self.calculate_digit_count(num)

    def add(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        min_exp = min(self.exp, other.exp)
        self.set_exponent(min_exp)
        other.set_exponent(min_exp)

        integral_part = self.number*self.sign + other.number*other.sign
        return InfinityFLoat(integral_part, min_exp)

    def sub(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        copy = InfinityFLoat(-1 * other.sign*other.number, other.exp)       # TODO: make this more efficient
        return self.add(copy)

    def mul(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    def div(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        if other.number == 0:
            raise ValueError("Can not divide by zero")
        return other.number

    # helper funcions __________________________________________________________________________
    def calculate_digit_count(self, number: int) -> int:
        count = 0
        num = abs(number)
        while num > 0:
            count += 1
            num //= 10
        return count

    def set_exponent(self, exp: int) -> None:   # only works with lowering exponent like 12*10^5 => 12_000*10^2
        dif = self.exp - exp
        self.exp = exp
        self.number *= 10**dif

    def get_string(self) -> str:
        return f'{self.number*self.sign} * 10^{self.exp} => {str(self)}'

    # magic methonds ___________________________________________________________________________
    def __str__(self):
        if self.number == 0:
            return "0"

        sign = "-" if self.sign == -1 else ""
        if self.exp >= 0:
            return f'{sign}{self.number * 10**(self.exp)}'

        exp = -self.exp
        integral_part = self.number // (10**exp)
        decimal_part = self.number - (integral_part * (10**exp))
        zeros = "0"*(exp - self.calculate_digit_count(decimal_part))

        return f'{sign}{integral_part}.{zeros}{decimal_part}'

    def __add__(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        if not isinstance(other, InfinityFLoat):
            raise TypeError("Operand must be an instance of InfinityFLoat")
        return self.add(other)

    def __sub__(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        if not isinstance(other, InfinityFLoat):
            raise TypeError("Operand must be an instance of InfinityFLoat")
        return self.sub(other)

    def __eq__(self, other: 'InfinityFLoat') -> bool:
        if not isinstance(other, InfinityFLoat):
            return False
        return self.exp == other.exp and self.number*self.sign == other.number*other.sign
