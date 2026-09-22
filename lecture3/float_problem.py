# this code example demonstrates the problems of float data type with certain values
from decimal import Decimal
import math

# this is a somewhat tedious feature of the float data type
number1 = float(0.1)
number2 = float(0.2)
print(f"Normal float/decimal numbers: {number1} + {number2} =")
print(number1 + number2)

# 0.1 is a problematic float value, or pretty much all values that are between 0 and 0.1
# this happens because of the method how computers handle floating numbers
# basically this is a problem in each programming languages, however, some programming languages "take care of this"
# automatically for the programmer

# one way is to use the decimal-module in Python
# note: remember to import decimal
number3 = Decimal("0.1")
number4 = Decimal("0.2")
print(f"Decimal numbers of the decimal-module: {number3} + {number4} =")
print(number3 + number4)