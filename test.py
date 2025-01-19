import unittest
from InfinityFLoat import InfinityFLoat



class Test(unittest.TestCase):

    def test_set(self):
        """Testing 'set' method"""

        float1 = InfinityFLoat()
        for i in range(-10, 0):
            float1.set(5, i)
            self.assertEqual(str(float1), "0." + "0"*(abs(i) - 1) + "5")
        for i in range(0, 11):
            float1.set(5, i)
            self.assertEqual(str(float1), "5" + "0"*i)

        # small numbers
        float1.set(1, -5)
        self.assertEqual(str(float1), "0.00001")

        float1.set(314, -2)
        self.assertEqual(str(float1), "3.14")
        float1.set(314, 2)
        self.assertEqual(str(float1), "31400")

        float1.set(1000, 0)
        self.assertEqual(str(float1), "1000")
        float1.set(1000, -6)
        self.assertEqual(str(float1), "0.001")
        
        # negative numbers
        float1.set(-100, 3)
        self.assertEqual(str(float1), "-100000")

        float1.set(-123, -3)
        self.assertEqual(str(float1), "-0.123")

        # zero
        float1.set(0, 10)
        self.assertEqual(str(float1), "0")        
        float1.set(0, -10)
        self.assertEqual(str(float1), "0")

        # zeros in the middle
        float1.set(1230000456, -5)
        self.assertEqual(str(float1), "12300.00456")
        float1.set(-1230000456, -5)
        self.assertEqual(str(float1), "-12300.00456")
        float1.set(1230000456, -7)
        self.assertEqual(str(float1), "123.0000456")

        # close to zero
        float1.set(1, -100)
        self.assertEqual(str(float1), "0." + "0" * 99 + "1")

        # big numbers
        float1.set(987654321987654321987654321, 10)
        self.assertEqual(str(float1), "9876543219876543219876543210000000000")

        float1.set(9876_543219876_543219876_543210000, -9)
        self.assertEqual(str(float1), "9876543219876543219876.54321")

        float1.set(123456789000000000123456789000000000, 0)
        self.assertEqual(str(float1), "123456789000000000123456789000000000")
        float1.set(1_000000000_000000000_000000000_000000000_123456789, -45)    # python -> 1.0 funny
        self.assertEqual(str(float1), "1.000000000000000000000000000000000000123456789")

        # big exponent
        float1.set(9999, 100)
        self.assertEqual(str(float1), "9999" + "0" * 100)
        float1.set(12, 1000)
        self.assertEqual(str(float1), "12" + "0" * 1000)


    def test_add(self):
        """Testing 'add' methon."""

        # small
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


        # small
        float1 = InfinityFLoat(500, -2) # 5
        float2 = InfinityFLoat(300, -2) # 3
        result = float1.add(float2)
        self.assertEqual(str(result), "8")

        float1 = InfinityFLoat(314, -2) # 3.14
        float2 = InfinityFLoat(2, 0)    # 2
        result = float1.add(float2)
        self.assertEqual(str(result), "5.14")
        float1 = InfinityFLoat(314, -2) # 3.14
        float2 = InfinityFLoat(2, -1)   # 0.2
        result = float1.add(float2)
        self.assertEqual(str(result), "3.34")
        float1 = InfinityFLoat(314, -2) # 3,14
        float2 = InfinityFLoat(2, -2)   # 0.02
        result = float1.add(float2)
        self.assertEqual(str(result), "3.16")
        float1 = InfinityFLoat(314, -2) # 3.14
        float2 = InfinityFLoat(2, -3)   # 0.002
        result = float1.add(float2)
        self.assertEqual(str(result), "3.142")

        # zero
        float1 = InfinityFLoat(123, 0)  # 123
        float2 = InfinityFLoat(0, 0)    # 0
        result = float1.add(float2)
        self.assertEqual(str(result), "123")
        float1 = InfinityFLoat(0, 0)    # 0
        float2 = InfinityFLoat(123, 0)  # 123
        result = float1.add(float2)
        self.assertEqual(str(result), "123")

        # negative
        float1 = InfinityFLoat(500, -2) # 5
        float2 = InfinityFLoat(-300, -2) # -3
        result = float1.add(float2)
        self.assertEqual(str(result), "2")

        float1 = InfinityFLoat(-500, -2)    # -5
        float2 = InfinityFLoat(-300, -2)    # -3
        result = float1.add(float2)
        self.assertEqual(str(result), "-8")

        # opposite sign
        float1 = InfinityFLoat(1000, -1)  # 100
        float2 = InfinityFLoat(-1000, -1)  # -100
        result = float1.add(float2)
        self.assertEqual(str(result), "0")

        # large exponent
        float1 = InfinityFLoat(1, 10)  # 10000000000
        float2 = InfinityFLoat(5, 5)   # 500000
        result = float1.add(float2)
        self.assertEqual(str(result), "10000500000")

        # very small
        float1 = InfinityFLoat(1, -10)  # 0.0000000001
        float2 = InfinityFLoat(1, -10)  # 0.0000000001
        result = float1.add(float2)
        self.assertEqual(str(result), "0.0000000002")

        # large and small
        float1 = InfinityFLoat(1, 5)    # 100000
        float2 = InfinityFLoat(1, -10)  # 0.0000000001
        result = float1.add(float2)
        self.assertEqual(str(result), "100000.0000000001")

        float1 = InfinityFLoat(1_000_000_000, 20)
        float2 = InfinityFLoat(1, -20)
        result = float1.add(float2)
        self.assertEqual(str(result), "1" + "0"*29 + ".00000000000000000001")

        float1 = InfinityFLoat(1, 100)
        float2 = InfinityFLoat(1, -20)
        result = float1.add(float2)
        self.assertEqual(str(result), "1" + "0"*100 + ".00000000000000000001")
        


        


if __name__ == "__main__":
    unittest.main()
