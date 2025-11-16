from typing import List, Tuple, Optional


def sum_even_odd(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate and return the sum of even and odd numbers separately.
    
    Args:
        numbers: List of integers to process.
        
    Returns:
        A tuple containing (sum_of_even_numbers, sum_of_odd_numbers).
    """
    sum_even = sum(n for n in numbers if n % 2 == 0)
    sum_odd = sum(n for n in numbers if n % 2 != 0)
    return sum_even, sum_odd


def parse_integers_from_input(user_input: str) -> Optional[List[int]]:
    """
    Parse a string of space or comma-separated integers.
    
    Args:
        user_input: String containing integers separated by spaces or commas.
        
    Returns:
        List of integers if parsing succeeds, None otherwise.
    """
    if not user_input.strip():
        return None
    
    # Normalize commas to spaces, split, and convert to integers
    parts = user_input.replace(",", " ").split()
    try:
        return [int(part) for part in parts]
    except ValueError:
        return None


def main() -> None:
    """Main function to handle user input and display results."""
    user_input = input("Enter integers separated by spaces or commas: ").strip()
    
    numbers = parse_integers_from_input(user_input)
    
    if numbers is None:
        if not user_input:
            print("No numbers provided.")
        else:
            print("Invalid input: please enter only integers.")
        return
    
    even_sum, odd_sum = sum_even_odd(numbers)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")


if __name__ == "__main__":
    main()