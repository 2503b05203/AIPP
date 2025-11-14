import sys

#!/usr/bin/env python3
"""
Check whether given user input is a palindrome.
Ignores non-alphanumeric characters and is case-insensitive.
"""


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch for ch in text if ch.isalnum()).casefold()
    return cleaned == cleaned[::-1]

def main():
    if len(sys.argv) > 1:
        # join args so user can pass phrases without quotes
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input("Enter text to check for palindrome: ")

    if is_palindrome(user_input):
        print("The input IS a palindrome.")
    else:
        print("The input is NOT a palindrome.")

if __name__ == "__main__":
    main()