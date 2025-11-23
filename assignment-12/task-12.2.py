def bubble_sort(lst):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    The function iterates through the list multiple times, comparing adjacent
    elements and swapping them if they are in the wrong order. This process
    "bubbles" the largest unsorted element to its correct position in each pass.

    Args:
        lst (list): The list of numbers to be sorted. The list is sorted in-place.
    """
    n = len(lst)
    # Traverse through all list elements
    for i in range(n):
        # A flag to optimize the sort. If no swaps occur in a pass, the list is sorted.
        swapped = False
        # Last i elements are already in place, so the inner loop range can be reduced.
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

if __name__ == "__main__":
    # Initialize a sample list of numbers
    my_list = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", my_list)

    # Call the bubble_sort function to sort the list
    bubble_sort(my_list)

    print("Sorted list:", my_list)