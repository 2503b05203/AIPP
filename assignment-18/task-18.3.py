def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive step: n! = n * (n-1)!
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Example usage
    try:
        test_number = int(input("Enter a non-negative integer to compute its factorial: "))
        result = factorial(test_number)
        print(f"The factorial of {test_number} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
