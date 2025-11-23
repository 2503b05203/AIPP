def linear_search(lst, value):
    """
    Performs a linear search for a value in a list.

    Args:
        lst (list): The list to be searched.
        value: The value to search for.

    Returns:
        int: The index of the value if found, otherwise -1.
    """
    for index, element in enumerate(lst):
        if element == value:
            return index  # Value found, return its index
    return -1  # Value not found after checking all elements

if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    try:
        # 3. Prompt the user to enter a value.
        user_input = input("Enter an integer to search for in the list: ")
        search_value = int(user_input)

        # 4. Use the linear_search() function to search for the value.
        index = linear_search(my_list, search_value)

        # 5. Print a message indicating the result.
        if index != -1:
            print(f"Value {search_value} found at index {index}.")
        else:
            print(f"Value {search_value} not found in the list.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
