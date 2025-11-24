def add(a, b):
    """
    Add two numbers and return the result.

    Parameters
    a & b -> either float or int

    Returns
    The sum of both inputs.
    """
    return a + b


def subtract(a, b):
    """
    Subtract from the first and return the result.

    Parameters
    a & b -> either float or int

    Returns

    The result of `a - b`.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Parameters
    a & b -> either float or int

    Returns
    The product of the two inputs.
    """
    return a * b


def divide(a, b):
    """
    Divide by the second and return the result.

    Parameters
    a & b -> either float or int

    Returns
    The result of `a / b` if valid, otherwise None.
    """
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

"""AI-generated arithmetic helper functions for Assignment 9."""


def ai_add(a, b):
    """
    Compute the sum of two numeric values.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The sum ``a + b``.
    """
    return a + b


def ai_subtract(a, b):
    """
    Compute the difference between two numeric values.

    Parameters
    ----------
    a : int or float
        Minuend.
    b : int or float
        Subtrahend.

    Returns
    -------
    int or float
        The result ``a - b``.
    """
    return a - b


def ai_multiply(a, b):
    """
    Compute the product of two numeric values.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The product ``a * b``.
    """
    return a * b


def ai_divide(a, b):
    """
    Compute the quotient of two numeric values.

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor.

    Returns
    -------
    float or None
        The quotient ``a / b`` if ``b`` is non-zero, otherwise ``None``.
    """
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b



# Main testing block
if __name__ == "__main__":
    # Demonstrating calculator functions with sample values
    print("Manual functions:")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
    print("Divide by zero attempt:", divide(10, 0))


    print("-" * 20)
    print("AI-generated functions:")

    print("Add by AI:", ai_add(10, 5))
    print("Subtract by AI:", ai_subtract(10, 5))
    print("Multiply by AI:", ai_multiply(10, 5))
    print("Divide by AI:", ai_divide(10, 5))
    print("Divide by zero attempt by AI:", ai_divide(10, 0))
