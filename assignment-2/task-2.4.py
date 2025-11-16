def sum_of_squares(numbers):
    """
    Returns the sum of the squares of the numbers in the input iterable.

    Example:
        sum_of_squares([1, 2, 3]) -> 14  (1^2 + 2^2 + 3^2)
    """
    return sum(x ** 2 for x in numbers)

if __name__ == "__main__":
    nums = input("Enter numbers separated by spaces: ")
    nums_list = [int(x) for x in nums.split()]
    result = sum_of_squares(nums_list)
    print("Sum of squares:", result)

