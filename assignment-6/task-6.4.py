def sum_to_n(n):
    """
    Calculates the sum of the first n natural numbers using both for and while loops.

    Args:
        n (int): The number up to which the sum is calculated.

    Returns:
        tuple: A tuple containing the sum calculated by the for loop and the sum 
        calculated by the while loop.
    """
    # Using a for loop
    sum_for = 0
    for i in range(1, n + 1):
        sum_for += i

    # Using a while loop
    sum_while = 0
    i = 1
    while i <= n:
        sum_while += i
        i += 1

    return sum_for, sum_while

# Example Usage
try:
    n_value_str = input("Enter a non-negative integer: ")
    n_value = int(n_value_str)
    if n_value < 0:
        print("Please enter a non-negative integer.")
    else:
        sum_for_loop, sum_while_loop = sum_to_n(n_value)
        print(f"Sum of first {n_value} natural numbers (for loop): {sum_for_loop}")
        print(f"Sum of first {n_value} natural numbers (while loop): {sum_while_loop}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
