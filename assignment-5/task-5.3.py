def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using recursion.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1.
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The index of the Fibonacci number to calculate (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        # Handle invalid input: Fibonacci sequence is defined for non-negative integers.
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        # Base case: The 0th Fibonacci number is 0.
        return 0
    elif n == 1:
        # Base case: The 1st Fibonacci number is 1.
        return 1
    else:
        # Recursive step: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    print("Fibonacci Sequence Calculator (Recursive)")

    while True:
        try:
            num = int(input("Enter a non-negative integer to find its Fibonacci number (or 'q' to quit): "))
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            
            # Call the recursive function to calculate the Fibonacci number
            result = fibonacci_recursive(num)
            print(f"The {num}th Fibonacci number is: {result}")
        except ValueError as e:
            if str(e) == "invalid literal for int() with base 10: 'q'":
                print("Exiting Fibonacci Calculator.")
                break
            else:
                print(f"Error: {e}. Please enter a valid non-negative integer.")
        except Exception as e:
            print(f"An unexpected error occurred : {e}")   