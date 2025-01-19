import unittest
from InfinityFLoat import InfinityFLoat



class Test(unittest.TestCase):
    # def setUp(self):
    #     """Object initialization"""
    #     self.my_float = InfinityFLoat()
    
    def create_string(self, integ: int, exp: int, res: float | int):
        return f'{integ} * 10^{exp} => {res}'

    def test_set(self):
        """Testing 'set' method"""

        float1 = InfinityFLoat()
        for i in range(-4, 10):
            float1.set(5, i)
            self.assertEqual(str(float1), self.create_string(5, i, 5*10**i))
        
        float1.set(314, -2)
        self.assertEqual(str(float1), self.create_string(314, -2, 3.14))
        float1.set(314, 2)
        self.assertEqual(str(float1), self.create_string(314, 2, 31400))

        float1.set(1000, 0)
        self.assertEqual(str(float1), self.create_string(1, 3, 1000))
        float1.set(1000, -6)
        self.assertEqual(str(float1), self.create_string(1, -3, 0.001))
        

        float1.set(1230000456, -5)
        self.assertEqual(str(float1), self.create_string(1230000456, -5, 12300.00456))
        float1.set(-1230000456, -5)
        self.assertEqual(str(float1), self.create_string(-1230000456, -5, -12300.00456))
        float1.set(1230000456, -7)
        self.assertEqual(str(float1), self.create_string(1230000456, -7, 123.0000456))

    def test_add(self):
        """Testing 'add' methon."""
        float1 = InfinityFLoat(314, -2)
        float2 = InfinityFLoat(2, 0)
        result = float1.add(float2)
        self.assertEqual(result, InfinityFLoat(514, -2))


        # small = InfinityFLoat(5, -2)
        # big = InfinityFLoat(3, 2)

        # another = small.add(big)
        # print(another)

        # small = InfinityFLoat(5, 5)
        # big = InfinityFLoat(123456, 10)

        # another = small.add(big)
        # print(another)
        # # + - adding
        # small = InfinityFLoat(-120, 0)
        # big = InfinityFLoat(-12, 1)

        # another = small.add(big)
        # print(another)     export PATH="/opt/homebrew/bin:/usr/bin/python3"

        # small = InfinityFLoat(-120, 0)
        # big = InfinityFLoat(12, 1)

        # another = small.add(big)
        # print(another)

if __name__ == "__main__":
    unittest.main()
