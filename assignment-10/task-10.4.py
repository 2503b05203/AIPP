from typing import List, Union

Numeric = Union[int, float]

def calculate_average(scores: List[Numeric]) -> float:
    """Calculates the average of a list of scores.

    Args:
        scores: A list of numeric scores.

    Returns:
        The average of the scores.
    """
    return sum(scores) / len(scores)

def find_highest(scores: List[Numeric]) -> Numeric:
    """Finds the highest score in a list.

    Args:
        scores: A list of numeric scores.

    Returns:
        The highest score in the list.
    """
    return max(scores)

def find_lowest(scores: List[Numeric]) -> Numeric:
    """Finds the lowest score in a list.

    Args:
        scores: A list of numeric scores.

    Returns:
        The lowest score in the list.
    """
    return min(scores)

def process_scores(scores: List[Numeric]):
    """
    Processes a list of scores to find and print the average, highest, and lowest values.

    Args:
        scores: A list of numeric scores.
    """
    if not scores:
        print("Cannot process an empty list of scores.")
        return

    try:
        avg = calculate_average(scores)
        highest = find_highest(scores)
        lowest = find_lowest(scores)

        print("--- Score Analysis ---")
        print(f"Average: {avg:.2f}")
        print(f"Highest: {highest}")
        print(f"Lowest:  {lowest}")
        print("----------------------")
    except Exception as e:
        print(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    sample_scores = [88, 92, 75, 98, 85, 89, 92, 100, 79]
    process_scores(sample_scores)
    process_scores([]) # Test with an empty list
