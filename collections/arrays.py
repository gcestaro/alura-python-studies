import array as arr
import numpy as np

"""
    Array docs: https://docs.python.org/3/library/array.html
    Avoid usage, efficient for numeric values. Normally use https://numpy.org/ instead.
"""

if __name__ == '__main__':
    array_of_doubles = arr.array("d", [1, 3.5])  # Float
    array_of_floats = arr.array("f", [1, 3.5])  # Float
    array_of_unsigned_long_long = arr.array("Q", [1, 2])  # Int
    array_of_signed_long_long = arr.array("q", [1, 3])  # Int
    array_of_unsigned_long = arr.array("L", [1, 4])  # Int
    array_of_signed_long = arr.array("l", [1, 5])  # Int
    array_of_unsigned_int = arr.array("I", [1, 6])  # Int
    array_of_signed_int = arr.array("i", [1, 7])  # Int
    array_of_unsigned_short = arr.array("H", [1, 8])  # Int
    array_of_signed_short = arr.array("h", [1, 8])  # Int
    array_of_unicode_char = arr.array("u", ["u"])  # Unicode character
    array_of_unsigned_char = arr.array("B", [1, 2])  # Int
    array_of_signed_char = arr.array("b", [4, 3])  # Int

    numbers = np.array([1, 2, 3.5])
    print(numbers)
    numbers += 3
    print(numbers)
