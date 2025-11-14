def reverse_string(s: str) -> str:
    """Return the reverse of the input string.

    Examples:
        >>> reverse_string('abc')
        'cba'

    Args:
        s: Input string.

    Returns:
        Reversed string.
    """
    return s[::-1]


if __name__ == "__main__":
    # Prompt the user for input and print the reversed string
    s = input("Enter a string to reverse: ").rstrip('\n')
    if s == "":
        print("No input provided. Exiting.")
    else:
        print(f"Reversed string: {reverse_string(s)}")
        