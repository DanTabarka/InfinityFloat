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
        float1 = InfinityFLoat(500, -2) # 5
        float2 = InfinityFLoat(300, -2) # 3
        self.assertEqual(str(float1 + float2), "8")
        self.assertEqual(float1, InfinityFLoat(500, -2))
        self.assertEqual(float2, InfinityFLoat(300, -2))

        float1.set(314, -2) # 3.14
        float2.set(2, 0)    # 2
        self.assertEqual(str(float1 + float2), "5.14")
        float2.set(2, -1)   # 0.2
        self.assertEqual(str(float1 + float2), "3.34")
        float2.set(2, -2)   # 0.02
        self.assertEqual(str(float1 + float2), "3.16")
        float2.set(2, -3)   # 0.002
        self.assertEqual(str(float1 + float2), "3.142")
        float2.set(2, -4)   # 0.0002
        self.assertEqual(str(float1 + float2), "3.1402")
        float2.set(2, -5)   # 0.00002
        self.assertEqual(str(float1 + float2), "3.14002")
        float2.set(2, -6)   # 0.000002
        self.assertEqual(str(float1 + float2), "3.140002")
        self.assertEqual(float1, InfinityFLoat(314, -2))
        self.assertEqual(float2, InfinityFLoat(2, -6))

        # zero
        float1.set(123, 0)  # 123
        float2.set(0, 0)    # 0
        self.assertEqual(str(float1 + float2), "123")
        self.assertEqual(str(float2 + float1), "123")
        self.assertEqual(str(float2 + float2), "0")
        self.assertEqual(str(float1 + float1), "246")

        # negative
        float1.set(500, -2) # 5
        float2.set(-300, -2) # -3
        self.assertEqual(str(float1 + float2), "2")
        self.assertEqual(str(float2 + float1), "2")

        # opposite sign
        float1.set(1000, -1)  # 100
        float2.set(-1000, -1)  # -100
        self.assertEqual(str(float1 + float2), "0")
        self.assertEqual(str(float2 + float1), "0")

        # large exponent
        float1.set(1, 10)  # 10000000000
        float2.set(5, 5)   # 500000
        self.assertEqual(str(float1 + float2), "10000500000")

        # very small
        float1.set(1, -10)  # 0.0000000001
        float2.set(1, -10)  # 0.0000000001
        self.assertEqual(str(float1 + float2), "0.0000000002")

        # large and small
        float1.set(1, 5)    # 100000
        float2.set(1, -10)  # 0.0000000001
        self.assertEqual(str(float1 + float2), "100000.0000000001")

        float1.set(1_000_000_000, 20)
        float2.set(1, -20)
        self.assertEqual(str(float1 + float2), "1" + "0"*29 + ".00000000000000000001")

        float1.set(1, 100)
        float2.set(1, -20)
        self.assertEqual(str(float1 + float2), "1" + "0"*100 + ".00000000000000000001")
        

    def test_sub(self):
        """Testing 'sub' methon."""

        # small
        float1 = InfinityFLoat(500, -2) # 5
        float2 = InfinityFLoat(300, -2) # 3
        self.assertEqual(str(float1 - float2), "2")

        float1.set(314, -2) # 3.14
        float2.set(2, 0)    # 2
        self.assertEqual(str(float1 - float2), "1.14")
        float2.set(2, -1)   # 0.2
        self.assertEqual(str(float1 - float2), "2.94")
        float2.set(2, -2)   # 0.02
        self.assertEqual(str(float1 - float2), "3.12")
        float2.set(2, -3)   # 0.002
        self.assertEqual(str(float1 - float2), "3.138")
        float2.set(2, -4)   # 0.0002
        self.assertEqual(str(float1 - float2), "3.1398")
        float2.set(2, -5)   # 0.00002
        self.assertEqual(str(float1 - float2), "3.13998")
        float2.set(2, -6)   # 0.000002
        self.assertEqual(str(float1 - float2), "3.139998")

        # zero
        float1.set(123, 0)  # 123
        float2.set(0, 0)    # 0
        self.assertEqual(str(float1 - float2), "123")
        self.assertEqual(str(float2 - float1), "-123")
        self.assertEqual(str(float2 - float2), "0")
        self.assertEqual(str(float1 - float1), "0")

        # negative
        float1.set(500, -2) # 5
        float2.set(-300, -2) # -3
        self.assertEqual(str(float1 - float2), "8")
        self.assertEqual(str(float2 - float1), "-8")

        # opposite sign
        float1.set(1000, -1)  # 100
        float2.set(-1000, -1)  # -100
        self.assertEqual(str(float1 - float2), "200")
        self.assertEqual(str(float2 - float1), "-200")

        # large exponent
        float1.set(1, 10)  # 10000000000
        float2.set(5, 5)   # 500000
        self.assertEqual(str(float1 - float2), "9999500000")
        self.assertEqual(str(float2 - float1), "-9999500000")

        # very small
        float1.set(1, -10)  # 0.0000000001
        float2.set(1, -10)  # 0.0000000001
        self.assertEqual(str(float1 - float2), "0")

        # large and small
        float1.set(1, 5)    # 100000
        float2.set(1, -10)  # 0.0000000001
        self.assertEqual(str(float1 - float2), "99999.9999999999")

        float1.set(1_000_000_000, 20)
        float2.set(1, -20)
        self.assertEqual(str(float1 - float2), "9"*29 + ".99999999999999999999")

        float1.set(1, 100)
        float2.set(1, -20)
        self.assertEqual(str(float1 - float2), "9"*100 + ".99999999999999999999")


    def test_mul(self):
        """Testing 'mul' methon."""

        # small numbers
        float1 = InfinityFLoat(5, 0)  # 5
        float2 = InfinityFLoat(3, 0)  # 3
        self.assertEqual(str(float1 * float2), "15")
        self.assertEqual(str(float2 * float1), "15")

        float1.set(314, -2)  # 3.14
        float2.set(2, 0)     # 2
        self.assertEqual(str(float1 * float2), "6.28")
        float2.set(2, -1)    # 0.2
        self.assertEqual(str(float1 * float2), "0.628")
        float2.set(2, -2)    # 0.02
        self.assertEqual(str(float1 * float2), "0.0628")
        float2.set(2, -3)    # 0.002
        self.assertEqual(str(float1 * float2), "0.00628")

        # zero
        float1.set(123, 0)  # 123
        float2.set(0, 0)    # 0
        self.assertEqual(str(float1 * float2), "0")
        self.assertEqual(str(float2 * float1), "0")
        self.assertEqual(str(float2 * float2), "0")
        self.assertEqual(str(float1 * float1), str(123*123))

        # negative numbers
        float1.set(500, -2)  # 5
        float2.set(-300, -2) # -3
        self.assertEqual(str(float1 * float2), "-15")
        self.assertEqual(str(float2 * float1), "-15")

        # opposite sign
        float1.set(1000, -1)  # 100
        float2.set(-1000, -1)  # -100
        self.assertEqual(str(float1 * float2), "-10000")
        self.assertEqual(str(float2 * float1), "-10000")

        # large exponent
        float1.set(1, 10)  # 10000000000
        float2.set(5, 5)   # 500000
        self.assertEqual(str(float1 * float2), "5000000000000000")

        # very small
        float1.set(1, -10)  # 0.0000000001
        float2.set(1, -10)  # 0.0000000001
        self.assertEqual(str(float1 * float2), "0.00000000000000000001")

        # large and small
        float1.set(1, 5)    # 100000
        float2.set(1, -10)  # 0.0000000001
        self.assertEqual(str(float1 * float2), "0.00001")

        float1.set(1_000_000_000, 20)
        float2.set(1, -20)
        self.assertEqual(str(float1 * float2), "1000000000")

        float1.set(1, 100)
        float2.set(1, -20)
        self.assertEqual(str(float1 * float2), "1" + "0" * 80)


    def test_div(self):
        """Testing 'div' methon.""" 
        
        # basic division
        float1 = InfinityFLoat(10, 0)  # 10
        float2 = InfinityFLoat(2, 0)   # 2
        self.assertEqual(str(float1 / float2), "5")

        float1.set(12345, 0)  # 12345
        float2.set(1, 0)      # 1
        self.assertEqual(str(float1 / float2), "12345")
        self.assertEqual(str(float1 / float1), "1")

        # fraction
        float1.set(3, 0)  # 3
        float2.set(2, 0)  # 2
        self.assertEqual(str(float1 / float2), "1.5")

        float1.set(49, 0)  # 49
        float2.set(8, 0)  # 8
        self.assertEqual(str(float1 / float2), "6.125")
        
        float1.set(9, 0)  # 9
        float2.set(16, 0)  # 16
        self.assertEqual(str(float1 / float2), "0.5625")
        float2.set(32, 0)  # 32
        self.assertEqual(str(float1 / float2), "0.28125")
        float2.set(64, 0)  # 64
        self.assertEqual(str(float1 / float2), "0.140625")

        float1.set(1, 3)  # 1000
        float2.set(3, 2)  # 300
        self.assertEqual(str(float1 / float2), "3." + "3" * (float1.digit_limit - 1))

        float1.set(5, 3)  # 5000
        float2.set(3, 0)  # 3
        self.assertEqual(str(float1 / float2), "1666." + "6" * (float1.digit_limit - 4))


        # large and small exponent
        float1.set(1, 10)  # 10000000000
        float2.set(1, 5)   # 100000
        self.assertEqual(str(float1 / float2), "100000")

        float1.set(1, -5)  # 0.00001
        float2.set(1, -10) # 0.0000000001
        self.assertEqual(str(float1 / float2), "100000")

        # negative numbers
        float1.set(-10, 0)  # -10
        float2.set(2, 0)    # 2
        self.assertEqual(str(float1 / float2), "-5")

        float1.set(10, 0)   # 10
        float2.set(-2, 0)   # -2
        self.assertEqual(str(float1 / float2), "-5")

        # small number
        float1.set(1, -10)  # 0.0000000001
        float2.set(1, 0)    # 1
        self.assertEqual(str(float1 / float2), "0.0000000001")

        # large number
        float1.set(1, 20)  # 100000000000000000000
        float2.set(1, 0)   # 1
        self.assertEqual(str(float1 / float2), "100000000000000000000")

        # zero
        float1 = InfinityFLoat(10, 0)
        zero = InfinityFLoat(0, 0)
        self.assertRaises(ValueError, float1.div, zero)
        self.assertRaises(ValueError, zero.div, zero)

        float2.set(10, 0) # 10
        self.assertEqual(str(zero / float2), "0")


    def test_digit_count(self):
        num = InfinityFLoat(123456789, 0, 3)
        self.assertEqual(str(num), "123000000")
        self.assertEqual(num.digit_count, 3)
        self.assertEqual(num.number, 123)

        num.set(123000000, -6)
        self.assertEqual(str(num), "123")

        # add
        num1 = InfinityFLoat(123000000, 0, 3)
        num2 = InfinityFLoat(123, 0, 3)
        self.assertEqual(str(num1 + num2), "123000000")

        num1.digit_limit = 6
        num2.digit_limit = 6
        self.assertEqual(str(num1 + num2), "123000000")
        num1.digit_limit = 7
        num2.digit_limit = 7
        self.assertEqual(str(num1 + num2), "123000100")
        num1.digit_limit = 8
        num2.digit_limit = 8
        self.assertEqual(str(num1 + num2), "123000120")
        num1.digit_limit = 9
        num2.digit_limit = 9
        self.assertEqual(str(num1 + num2), "123000123")
        num1.digit_limit = 10
        num2.digit_limit = 10
        self.assertEqual(str(num1 + num2), "123000123")

        # sub
        num1 = InfinityFLoat(123000000, 0, 3)
        num2 = InfinityFLoat(123, 0, 3)
        self.assertEqual(str(num1 - num2), "123000000")

        num1.digit_limit = 6
        num2.digit_limit = 6
        self.assertEqual(str(num1 - num2), "123000000")
        num1.digit_limit = 7
        num2.digit_limit = 7
        self.assertEqual(str(num1 - num2), "122999900")
        num1.digit_limit = 8
        num2.digit_limit = 8
        self.assertEqual(str(num1 - num2), "122999880")
        num1.digit_limit = 9
        num2.digit_limit = 9
        self.assertEqual(str(num1 - num2), "122999877")
        num1.digit_limit = 10
        num2.digit_limit = 10
        self.assertEqual(str(num1 - num2), "122999877")



if __name__ == "__main__":
    unittest.main()
