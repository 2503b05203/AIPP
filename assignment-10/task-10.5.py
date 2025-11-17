from typing import Union

def safe_divide(a: float, b: float) -> Union[float, str]:
    """
    Safely divides two numbers, handling potential division by zero and type errors.

    This function attempts to divide the numerator 'a' by the denominator 'b'.
    It includes error handling to catch common issues that can occur during
    a division operation.

    Args:
        a (float): The numerator (the number to be divided).
        b (float): The denominator (the number to divide by).

    Returns:
        Union[float, str]: The result of the division if successful, or an
        error message string if a ZeroDivisionError or TypeError occurs.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Testing Safe Division ---")

    # Test case 1: Valid division
    print(f"10 / 2 = {safe_divide(10, 2)}")

    # Test case 2: Division by zero
    print(f"10 / 0 = {safe_divide(10, 0)}")

    # Test case 3: Invalid input type
    print(f"10 / 'a' = {safe_divide(10, 'a')}")
