import re

def is_valid_email(email):
    """
    Validates an email address based on specific requirements.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Requirement 1: The email must contain both the @ and . characters.
    if '@' not in email or '.' not in email:
        return False

    # Requirement 2: The email must not start or end with special characters.
    # Define a set of special characters to check for at the beginning and end.
    special_chars = "!#$%&'*+-/=?^_`{|}~"
    if email[0] in special_chars or email[-1] in special_chars:
        return False

    # Requirement 3: The email should not contain multiple @ symbols.
    if email.count('@') > 1:
        return False

    # Additional common email validation (e.g., no special chars before @, domain part)
    # This is a more robust regex for general email validation, but we'll focus on the specified requirements.
    # For the given requirements, the above checks are sufficient.
    # If more complex validation is needed, a regex like the one below would be used:
    # if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
    #     return False

    return True

# Test cases for is_valid_email function
def run_tests():
    test_cases = [
        # Valid emails
        ("test@example.com", True, "Valid email"),
        ("john.doe@sub.domain.co.uk", True, "Valid email with subdomains"),
        ("user123@domain.net", True, "Valid email with numbers"),
        ("first.last@company.org", True, "Valid email with dot in local part"),

        # Invalid emails - Missing @ or .
        ("testexample.com", False, "Missing @"),
        ("test@examplecom", False, "Missing ."),
        ("testexamplecom", False, "Missing @ and."),

        # Invalid emails - Starts or ends with special characters
        (".test@example.com", False, "Starts with dot"),
        ("test@example.com.", False, "Ends with dot"),
        ("-test@example.com", False, "Starts with hyphen"),
        ("test@example.com-", False, "Ends with hyphen"),
        ("_test@example.com", False, "Starts with underscore"),
        ("test@example.com_", False, "Ends with underscore"),

        # Invalid emails - Multiple @ symbols
        ("test@example@com", False, "Multiple @ symbols"),

        # Edge cases
        ("", False, "Empty string"),
        ("a@b.c", True, "Shortest valid email"),
        ("test@.com", False, "Domain starts with dot"),
        ("test@com.", False, "Domain ends with dot"),
        ("test@example..com", False, "Multiple dots in domain (though some systems allow)"),
        ("test@example", False, "Missing top-level domain"),
        ("test@123.456", True, "IP address-like domain (valid by current rules)"),
        ("!test@example.com", False, "Starts with special char"),
        ("test@example.com!", False, "Ends with special char"),
    ]

    for email, expected, description in test_cases:
        result = is_valid_email(email)
        if result != expected:
            print(f"Test failed for '{email}' ({description}). Expected {expected}, got {result}")
        else:
            print(f"Test passed for '{email}' ({description}).")


if __name__ == "__main__":
    run_tests()