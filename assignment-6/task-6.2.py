def print_multiples_of_ten(number):
    """Prints the first 10 multiples of a given number."""
    print(f"First 10 multiples of {number}:")
    for i in range(1, 11):
        print(number * i)

# Example Usage
print_multiples_of_ten(5)
print_multiples_of_ten(7)
