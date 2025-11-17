def assign_grade(score):
    """
    Assigns a letter grade based on a numeric score from 0 to 100.

    - 90-100: 'A'
    - 80-89:  'B'
    - 70-79:  'C'
    - 60-69:  'D'
    - <60:    'F'

    Args:
        score (int or float): The student's score.

    Returns:
        str: The corresponding letter grade.

    Raises:
        ValueError: If the score is not a number or is outside the valid range of 0-100.
    """
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a numeric value.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
def run_grade_tests():
    """
    Runs a suite of test cases for the assign_grade function,
    covering typical values, boundary conditions, and invalid inputs.
    """
    # Format: (input_score, expected_output, description)
    # For invalid inputs, expected_output is the exception type (e.g., ValueError).
    test_cases = [
        # Grade A: 90-100
        (95, 'A', "Typical score for grade A"),
        (90, 'A', "Lower boundary for grade A"),
        (100, 'A', "Upper boundary for grade A"),

        # Grade B: 80-89
        (85, 'B', "Typical score for grade B"),
        (80, 'B', "Lower boundary for grade B"),
        (89, 'B', "Upper boundary for grade B"),
        (89.9, 'B', "Upper boundary for grade B (float)"),

        # Grade C: 70-79
        (75, 'C', "Typical score for grade C"),
        (70, 'C', "Lower boundary for grade C"),
        (79, 'C', "Upper boundary for grade C"),

        # Grade D: 60-69
        (65, 'D', "Typical score for grade D"),
        (60, 'D', "Lower boundary for grade D"),
        (69, 'D', "Upper boundary for grade D"),

        # Grade F: <60
        (30, 'F', "Typical score for grade F"),
        (0, 'F', "Lower boundary for valid scores (Grade F)"),
        (59, 'F', "Upper boundary for grade F"),
        (59.9, 'F', "Upper boundary for grade F (float)"),

        # --- Invalid Inputs ---
        # Scores outside the 0-100 range
        (105, ValueError, "Score above 100"),
        (100.1, ValueError, "Score just above 100"),
        (-5, ValueError, "Negative score"),
        (-0.1, ValueError, "Slightly negative score"),

        # Non-numeric inputs
        ("eighty", ValueError, "String input"),
        ("90", ValueError, "String number input"),
        (None, ValueError, "None input"),
        ([85], ValueError, "List input"),
    ]

    print("--- Running Grade Assignment Tests ---")
    passed_count = 0
    failed_count = 0

    for score, expected, description in test_cases:
        try:
            # Case 1: Testing for a valid return value
            if not isinstance(expected, type) or not issubclass(expected, BaseException):
                result = assign_grade(score)
                if result == expected:
                    print(f"✅ PASS: assign_grade({score}) -> '{result}' ({description})")
                    passed_count += 1
                else:
                    print(f"❌ FAIL: assign_grade({score}) -> Expected '{expected}', but got '{result}' ({description})")
                    failed_count += 1
            # Case 2: Testing for an expected exception
            else:
                assign_grade(score)
                # If this line is reached, the expected exception was not raised
                print(f"❌ FAIL: assign_grade({score}) -> Expected {expected.__name__}, but no exception was raised. ({description})")
                failed_count += 1
        except Exception as e:
            # Check if the raised exception is the one we expected
            if isinstance(e, expected):
                print(f"✅ PASS: assign_grade({score}) -> Raised {type(e).__name__} as expected. ({description})")
                passed_count += 1
            else:
                print(f"❌ FAIL: assign_grade({score}) -> Expected {expected.__name__}, but got {type(e).__name__}. ({description})")
                failed_count += 1

    print("\n--- Test Summary ---")
    print(f"Total tests: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print("--------------------")


if __name__ == "__main__":
    # You can run the tests by calling the function
    run_grade_tests()

