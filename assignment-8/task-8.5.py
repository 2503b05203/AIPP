import datetime
from typing import Optional

def convert_date_format(date_str: str) -> Optional[str]:
    """
    Converts a date string from "YYYY-MM-DD" to "DD-MM-YYYY".

    Args:
        date_str (str): The date string in "YYYY-MM-DD" format.

    Returns:
        Optional[str]: The converted date string in "DD-MM-YYYY" format,
                       or None if the input is invalid, empty, or not a valid date.
    """
    if not isinstance(date_str, str) or not date_str:
        return None

    try:
        # Attempt to parse the string using the expected format.
        # This also validates the date's correctness (e.g., month <= 12, day <= 31).
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        # Format the date object into the desired "DD-MM-YYYY" string.
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        # This exception is raised if the string doesn't match the format
        # or represents an invalid date (e.g., "2023-02-30").
        return None

def run_date_format_tests():
    """
    Runs a suite of test cases for the convert_date_format function.
    """
    # Format: (input_date, expected_output, description)
    test_cases = [
        # --- Valid Inputs ---
        ("2023-10-15", "15-10-2023", "Standard valid date"),
        ("1999-07-25", "25-07-1999", "Another valid date"),

        # --- Boundary Cases ---
        ("2024-01-01", "01-01-2024", "Start of a leap year"),
        ("2023-12-31", "31-12-2023", "End of a non-leap year"),
        ("2024-02-29", "29-02-2024", "Leap day"),

        # --- Edge Cases ---
        ("2023-03-05", "05-03-2023", "Single-digit day and month"),
        ("2023-09-01", "01-09-2023", "Single-digit day"),
        ("2023-01-11", "11-01-2023", "Single-digit month"),

        # --- Invalid Inputs ---
        ("2023-13-40", None, "Invalid month and day"),
        ("2023-11-31", None, "Invalid day for the month (Nov has 30 days)"),
        ("2023-02-29", None, "Invalid leap day in a non-leap year"),
        ("15-10-2023", None, "Incorrect input format (DD-MM-YYYY)"),
        ("2023/10/15", None, "Incorrect separator"),
        ("not-a-date", None, "Non-date string"),
        ("2023-1-5", None, "Missing leading zeros"),
        ("", None, "Empty string"),
        (None, None, "None input"),
        (20231015, None, "Integer input"),
    ]

    print("--- Running Date Format Conversion Tests ---")
    passed_count = 0
    failed_count = 0

    for date_str, expected, description in test_cases:
        try:
            result = convert_date_format(date_str)
            if result == expected:
                print(f"✅ PASS: convert_date_format('{date_str}') -> '{result}' ({description})")
                passed_count += 1
            else:
                print(f"❌ FAIL: convert_date_format('{date_str}') -> Expected '{expected}', but got '{result}' ({description})")
                failed_count += 1
        except Exception as e:
            print(f"❌ ERROR: convert_date_format('{date_str}') -> Raised an unexpected exception: {e} ({description})")
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
    run_date_format_tests()
