from typing import List, Tuple

def process_and_print_sums(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum of even and odd numbers from a list, prints both sums,
    and returns them as a tuple.

    Args:
        numbers: A list of integers to process.

    Returns:
        A tuple containing (sum_of_even_numbers, sum_of_odd_numbers).
    """
    sum_even = sum(n for n in numbers if n % 2 == 0)
    sum_odd = sum(n for n in numbers if n % 2 != 0)

    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")

    return sum_even, sum_odd

if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Processing the list: {sample_numbers}")
    
    even_total, odd_total = process_and_print_sums(sample_numbers)
    
    print(f"\nFunction returned: ({even_total}, {odd_total})")

    print("-" * 20)

    print("Processing an empty list: []")
    process_and_print_sums([])
