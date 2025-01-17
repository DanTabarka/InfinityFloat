

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
        self.number, self.exp = self.base_form(number, exponent_shift)
    
    def base_form(self, number: int, exponent_shift: int) -> tuple[int, int]:
        while number % 10 == 0:
            number //= 10
            exponent_shift += 1
        return number, exponent_shift
    
    def add(self, float: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    def sub(self, float: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    def mul(self, float: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    def div(self, float: 'InfinityFLoat') -> 'InfinityFLoat':
        pass
    
    # helper funcions __________________________________________________________________________
    def digit_count(self, number: int) -> int:
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count 

    def __str__(self):
        if self.exp >= 0:
            return f'{self.number} * 10^{self.exp} => {self.number * 10**(self.exp)}'
        
        exp = -self.exp
        integral_part = self.number // (10**exp)
        zeros = "0"*(exp - self.digit_count(self.number))
        decimal_part = self.number - (integral_part * (10**exp))

        return f'{self.number} * 10^{self.exp} => {integral_part},{zeros}{decimal_part}'


my_float = InfinityFLoat(314, -2)
print(my_float)
my_float = InfinityFLoat(314, 2)
print(my_float)
my_float = InfinityFLoat(31415926535, -100)
print(my_float)

my_float = InfinityFLoat(30000, 0)
print(my_float)

