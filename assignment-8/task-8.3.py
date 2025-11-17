import string

def is_sentence_palindrome(sentence: str) -> bool:
    """
    Checks if a sentence is a palindrome, ignoring case, punctuation, and spaces.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward.

    Args:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a palindrome, False otherwise.
    """
    if not isinstance(sentence, str):
        return False

    # Create a new string with only alphanumeric characters, in lowercase
    cleaned_chars = [char.lower() for char in sentence if char.isalnum()]
    cleaned_sentence = "".join(cleaned_chars)

    # Check if the cleaned string is equal to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]

def run_palindrome_tests():
    """
    Runs a suite of AI-generated test cases for the is_sentence_palindrome function.
    """
    # Format: (input_sentence, expected_output, description)
    test_cases = [
        # --- True Palindromes ---
        ("A man, a plan, a canal: Panama", True, "Classic complex palindrome"),
        ("Was it a car or a cat I saw?", True, "Palindrome with question mark"),
        ("No 'x' in 'Nixon'", True, "Palindrome with quotes"),
        ("Madam, in Eden, I'm Adam.", True, "Palindrome with comma and apostrophe"),
        ("racecar", True, "Simple single-word palindrome"),
        ("Level", True, "Single-word palindrome with mixed case"),
        ("12321", True, "Numeric palindrome as a string"),
        ("Go hang a salami, I'm a lasagna hog.", True, "Another complex palindrome"),
        ("Step on no pets", True, "Palindrome with spaces"),

        # --- False Palindromes ---
        ("hello world", False, "Simple non-palindrome"),
        ("This is not a palindrome", False, "Longer non-palindrome sentence"),
        ("palindrome", False, "A word that is not a palindrome"),
        ("A man, a plan, a canal: Suez", False, "Almost a palindrome"),
        ("12345", False, "Non-palindrome number string"),

        # --- Edge Cases ---
        ("", True, "Empty string (reads the same forwards and backwards)"),
        (" ", True, "String with only a space"),
        ("?", True, "String with only punctuation"),
        ("a", True, "Single character string"),
        ("aa", True, "Two-character palindrome"),
        ("ab", False, "Two-character non-palindrome"),

        # --- Invalid Inputs (should return False) ---
        (None, False, "None input"),
        (12321, False, "Integer input"),
        (["a", "b", "a"], False, "List input"),
    ]

    print("--- Running Sentence Palindrome Tests ---")
    passed_count = 0
    failed_count = 0

    for sentence, expected, description in test_cases:
        try:
            result = is_sentence_palindrome(sentence)
            if result == expected:
                # Truncate long sentences for cleaner output
                display_sentence = (sentence[:30] + '...') if isinstance(sentence, str) and len(sentence) > 33 else sentence
                print(f"✅ PASS: is_sentence_palindrome('{display_sentence}') -> {result} ({description})")
                passed_count += 1
            else:
                print(f"❌ FAIL: is_sentence_palindrome('{sentence}') -> Expected {expected}, but got {result} ({description})")
                failed_count += 1
        except Exception as e:
            print(f"❌ ERROR: is_sentence_palindrome('{sentence}') -> Raised an unexpected exception: {e} ({description})")
            failed_count += 1

    print("\n--- Test Summary ---")
    print(f"Total tests: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print("--------------------")

    if failed_count == 0:
        print("\nAll tests passed successfully!")
    else:
        print(f"\n{failed_count} test(s) failed.")

if __name__ == "__main__":
    run_palindrome_tests()