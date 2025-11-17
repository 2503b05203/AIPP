"""A simple calculator module with basic arithmetic operations.

This module provides functions to perform addition, subtraction,
multiplication, and division. Each function is designed to handle
numeric inputs (integers or floats) and includes detailed documentation
on its usage, parameters, and return values.

Functions
---------
add(a, b)
    Computes the sum of two numbers.
subtract(a, b)
    Computes the difference between two numbers.
multiply(a, b)
    Computes the product of two numbers.
divide(a, b)
    Computes the division of two numbers, with handling for division by zero.
"""

from typing import Union

Numeric = Union[int, float]

def add(a: Numeric, b: Numeric) -> Numeric:
    """Computes the sum of two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The sum of `a` and `b`.
    """
    return a + b

def subtract(a: Numeric, b: Numeric) -> Numeric:
    """Computes the difference between two numbers.

    Parameters
    ----------
    a : int or float
        The number to be subtracted from.
    b : int or float
        The number to subtract.

    Returns
    -------
    int or float
        The result of `a` minus `b`.
    """
    return a - b

def multiply(a: Numeric, b: Numeric) -> Numeric:
    """Computes the product of two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The product of `a` and `b`.
    """
    return a * b

def divide(a: Numeric, b: Numeric) -> float:
    """Computes the division of two numbers.

    This function divides the first number by the second. It includes a
    check to prevent division by zero.

    Parameters
    ----------
    a : int or float
        The numerator (dividend).
    b : int or float
        The denominator (divisor).

    Returns
    -------
    float
        The result of `a` divided by `b`.

    Raises
    ------
    ValueError
        If the divisor `b` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # --- Example Usage ---
    num1, num2 = 10, 5

    print(f"--- Simple Calculator Operations ---")
    print(f"Numbers: {num1}, {num2}\n")

    # Addition
    sum_result = add(num1, num2)
    print(f"Addition:       {num1} + {num2} = {sum_result}")

    # Subtraction
    diff_result = subtract(num1, num2)
    print(f"Subtraction:    {num1} - {num2} = {diff_result}")

    # Multiplication
    prod_result = multiply(num1, num2)
    print(f"Multiplication: {num1} * {num2} = {prod_result}")

    # Division
    try:
        quotient_result = divide(num1, num2)
        print(f"Division:       {num1} / {num2} = {quotient_result}")
        # Test division by zero
        print(f"\nAttempting to divide by zero...")
        divide(num1, 0)
    except ValueError as e:
        print(f"Error: {e}")
