from typing import List, Tuple

def process_and_print_sums(numbers: List[int]) -> Tuple[int, int]:
    """
    from a list of numbers, adds up all the even ones and all the odd ones,
    prints the two totals as a pair.

    Args:
        numbers: A list of whole numbers (integers).

    Returns:
        A tuple like (total_of_evens, total_of_odds).
    """
    # Add up all the even numbers
    sum_even = sum(n for n in numbers if n % 2 == 0)

    # Add up all the odd numbers
    sum_odd = sum(n for n in numbers if n % 2 != 0)

    # Print the results so the user can see what happened
    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")

    return sum_even, sum_odd


def process_and_print_sums_ai(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute parity-specific totals and emit a short diagnostic summary.

    Args:
        numbers: Sequence of integers that may include positive, negative,
            or zero-valued entries.

    Returns:
        Tuple where index 0 holds the sum of even inputs and index 1 stores
        the sum of odd inputs.
    """
    # Separate the accumulation logic by parity to keep the intent explicit.
    even_total = sum(value for value in numbers if value % 2 == 0)

    # Reuse the same traversal strategy for odd values to maintain symmetry.
    odd_total = sum(value for value in numbers if value % 2 != 0)

    # Provide a concise readout that mirrors the original helper's behavior.
    print(f"[AI] even sum -> {even_total}")
    print(f"[AI] odd sum  -> {odd_total}")

    return even_total, odd_total


if __name__ == "__main__":
    # A sample list so we can try out the function
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Processing the list: {sample_numbers}")
    
    # Run the function and store what it returns
    even_total, odd_total = process_and_print_sums(sample_numbers)
    
    print(f"\nFunction returned: ({even_total}, {odd_total})")

    print("-" * 20)


    print("\n--- AI-documented variant ---")
    print(f"Processing the list: {sample_numbers}")
    ai_even_total, ai_odd_total = process_and_print_sums_ai(sample_numbers)
    print(f"\nAI function returned: ({ai_even_total}, {ai_odd_total})")