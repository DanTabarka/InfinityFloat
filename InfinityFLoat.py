
class InfinityFLoat:
    """
    A class for working with decimal numbers of infinite precision.

    This class represents numbers with a base value (`number`) and an
    associated exponent (`exponent_shift`) that scales the base value by
    a power of ten. It enables precise arithmetic and representation of
    numbers in the form `number * 10^(exponent_shift)`.

    Atributes:
        number         (int): The base integer value of the number.
        exp            (int): The power of 10 by which the base value is scaled.
                              For example, 314 with an exponent_shift of -2
                              represents the number 3.14 (314 * 10^(-2)).
        sign           (int): -1 or 1
        digit_count    (int): digit count of number
        digit_limit    (int): limit of digits (precission)
    """
    def __init__(self, number=0, exponent_shift=0, digit_limit=1000):
        self.digit_limit = digit_limit
        self.set(number, exponent_shift)

    def set(self, number: int, exponent_shift: int) -> None:
        self.base_form(number, exponent_shift)
        self.cut_number()

    def base_form(self, number: int, exponent_shift: int) -> None:
        self.sign = 1 if number >= 0 else -1
        num = abs(number)
        while num % 10 == 0 and num > 0:
            num //= 10
            exponent_shift += 1
        self.number = num
        self.exp = exponent_shift
        self.digit_count = self.calculate_digit_count(num)
    
    def cut_number(self) -> None:
        if self.digit_count > self.digit_limit:
            diference = self.digit_count - self.digit_limit
            self.exp += diference
            self.number //= 10**diference
            self.digit_count = self.digit_limit

    def add(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        max_digit_limit = max(self.digit_limit, other.digit_limit)
        copy_other = InfinityFLoat(other.sign*other.number, other.exp, max_digit_limit)       # TODO: make this more efficient
        copy_self = InfinityFLoat(self.sign*self.number, self.exp, max_digit_limit)          # TODO: make this more efficient
        min_exp = min(copy_self.exp, copy_other.exp)
        copy_self.set_exponent(min_exp)
        copy_other.set_exponent(min_exp)

        digit_count_self = self.calculate_digit_count(copy_self.number)
        digit_count_other = self.calculate_digit_count(copy_other.number)
        to_lower_exp = max(digit_count_other, digit_count_self) - max_digit_limit      # to calculate if shift is needed
        if to_lower_exp > 0:    
            copy_self.exp += to_lower_exp
            copy_self.number //= 10**to_lower_exp
            copy_other.exp += to_lower_exp
            copy_other.number //= 10**to_lower_exp
            min_exp += to_lower_exp

        integral_part = copy_self.number*copy_self.sign + copy_other.number*copy_other.sign
        return InfinityFLoat(integral_part, min_exp, max_digit_limit)                       # TODO: make min_digit_limit more efficient

    def sub(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        max_digit_limit = max(self.digit_limit, other.digit_limit)
        copy = InfinityFLoat(-1 * other.sign*other.number, other.exp, max_digit_limit)       # TODO: make this more efficient
        return self.add(copy)

    def mul(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        max_digit_limit = max(self.digit_limit, other.digit_limit)
        integral_part = self.sign * self.number * other.number * other.sign
        exp = self.exp + other.exp
        return InfinityFLoat(integral_part, exp, max_digit_limit)

    def div(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        if other.number == 0:
            raise ValueError("Can not divide by zero")
        
        max_digit_limit = max(self.digit_limit, other.digit_limit)
        copy_other = InfinityFLoat(other.sign*other.number, other.exp)       # TODO: make this more efficient
        copy_self = InfinityFLoat(self.sign*self.number, self.exp)          # TODO: make this more efficient
        exp = min(copy_self.exp, copy_other.exp)
        copy_self.set_exponent(exp)
        copy_other.set_exponent(exp)

        integral_part = copy_self.number // copy_other.number
        remain = copy_self.number - integral_part*copy_other.number
        digit_counter = self.calculate_digit_count(integral_part)
        exp = 0
        while remain > 0 and digit_counter < self.digit_limit:
            digit_counter += 1
            next_digit = (remain * 10) // copy_other.number
            integral_part = (integral_part * 10) + next_digit
            remain = (remain * 10) - next_digit * copy_other.number
            exp -= 1

        return InfinityFLoat(integral_part * copy_self.sign * copy_other.sign, exp, max_digit_limit)

    # helper funcions __________________________________________________________________________
    def calculate_digit_count(self, number: int) -> int:
        count = 0
        num = abs(number)
        while num > 0:
            count += 1
            num //= 10
        return count

    def set_exponent(self, exp: int) -> None:   # only works with lowering exponent like 12*10^5 => 12_000*10^2
        dif = self.exp - exp                    # !!!damage the number!!!, it will not be in the base form
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

    def __mul__(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        if not isinstance(other, InfinityFLoat):
            raise TypeError("Operand must be an instance of InfinityFLoat")
        return self.mul(other)
    
    def __truediv__(self, other: 'InfinityFLoat') -> 'InfinityFLoat':
        if not isinstance(other, InfinityFLoat):
            raise TypeError("Operand must be an instance of InfinityFLoat")
        return self.div(other)
    
    # __floordiv__(self, other): Celočíselné dělení (//).
    # __mod__(self, other): Zbytek po dělení (%).
    # __pow__(self, other[, modulo]): Umocnění (**).
    # __abs__(self): Absolutní hodnota (abs(a)).

    def __eq__(self, other: 'InfinityFLoat') -> bool:
        if not isinstance(other, InfinityFLoat):
            return False
        return self.exp == other.exp and self.number*self.sign == other.number*other.sign


