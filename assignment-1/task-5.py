from typing import List

#!/usr/bin/env python3
# task-5.py
# Read a list of numbers from user input and print the largest.


def find_largest(numbers: List[float]) -> float:
    """Return the largest number in the list. Raises ValueError on empty list."""
    if not numbers:
        raise ValueError("empty list")
    return max(numbers)

def parse_numbers(s: str) -> List[float]:
    """Parse a string of numbers separated by spaces or commas into a list of floats."""
    if not s.strip():
        return []
    parts = s.replace(",", " ").split()
    nums = []
    for p in parts:
        try:
            nums.append(float(p))
        except ValueError:
            raise ValueError(f"invalid number: {p}")
    return nums

def main():
    try:
        s = input("Enter numbers separated by spaces or commas: ")
        nums = parse_numbers(s)
        if not nums:
            print("No numbers provided.")
            return
        largest = find_largest(nums)
        # Print as int if it's an integer value
        if largest.is_integer():
            print(int(largest))
        else:
            print(largest)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()