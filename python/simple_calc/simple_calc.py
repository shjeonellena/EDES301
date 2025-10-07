# -*- coding: utf-8 -*-
from __future__ import print_function, division  # Py2 compatibility for print and /
import operator
import sys

# ---- Py2/3 input compatibility ----
try:
    input_func = raw_input   # Python 2
except NameError:
    input_func = input       # Python 3

operators = {
    "+":  operator.add,
    "-":  operator.sub,
    "*":  operator.mul,
    "/":  operator.truediv,  # consistent true division across Py2/3
    ">>": operator.rshift,
    "<<": operator.lshift,
    "%":  operator.mod,
    "**": operator.pow,
}

BITWISE_OPS = {"<<", ">>"}

def get_user_input():
    """
    Returns: (num1, num2, func) or (None, None, None) if invalid.
    - Bitwise ops (<<, >>) use int operands
    - All other ops use float operands
    """
    try:
        # Read raw strings first so we can decide how to cast based on operator
        s1 = input_func("Enter first number : ")
        s2 = input_func("Enter second number: ")
        op = input_func("Enter function (valid values are +, -, *, /, >>, <<, %, **): ").strip()

        func = operators.get(op)
        if func is None:
            print("Invalid operator.")
            return (None, None, None)

        if op in BITWISE_OPS:
            # Bitwise requires integers
            n1 = int(float(s1))  # allow "8" or "8.0"
            n2 = int(float(s2))
        else:
            # Normal math: allow floats
            n1 = float(s1)
            n2 = float(s2)

        return (n1, n2, func)

    except ValueError:
        print("Invalid number input.")
        return (None, None, None)
    except Exception as e:
        print("Error reading input:", e)
        return (None, None, None)

if __name__ == "__main__":
    while True:
        num1, num2, func = get_user_input()
        if (num1 is None) or (num2 is None) or (func is None):
            break

        try:
            result = func(num1, num2)
            print(result)
        except ZeroDivisionError:
            print("Error: division by zero.")
        except TypeError as e:
            # e.g., trying bitwise with non-int (shouldn't happen due to casting above)
            print("Type error:", e)
        except Exception as e:
            print("Unexpected error:", e)

        # Repeat?
        again = input_func("Compute another? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break
