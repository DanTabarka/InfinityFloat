
# InfinityFloat: Master of Infinite Precision 🧮✨

Ever wished you could handle decimal numbers with absolute precision, without those pesky floating-point errors? Say hello to **InfinityFloat**, the class that makes your decimals shine brighter than your math teacher’s enthusiasm for pi! 🎉

---

## What is InfinityFloat? 🤔  
It’s a Python class for working with decimal numbers that laugh in the face of floating-point imprecision. InfinityFloat represents numbers in the form:  

So, `314` with an `exponent_shift` of `-2` becomes `3.14`. Yes, it's math, but it's also magic. 🪄

---

## Why Does This Exist? 🤷  
Honestly? This project was just for fun. 😄 But also because we hate rounding errors more than forgetting a semicolon in C. If you're tired of `0.1 + 0.2` being anything but `0.3`, you're in the right place.

---

## How It Works 🚀 
Python integers have infinity precision, so why not use them to represent floating-point numbers with perfect accuracy? That's exactly what this class does!
The class represents a number with:  
- **`number` (int):** The base integer value.  
- **`exponent_shift` (int):** The power of 10 by which the base is scaled.  

Example:
```python
InfinityFloat(314, -2)  # Represents 3.14
InfinityFloat(3, 3)  # Represents 3000
InfinityFloat(123456789, -8)  # Represents 1.23456789
