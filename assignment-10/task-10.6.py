def grade(score):
    """
    Converts a numerical score into a letter grade based on a predefined scale.
    """
    # This list maps the minimum score required for each grade.
    # It must be sorted in descending order of score.
    GRADE_MAP = [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
    ]

    for min_score, letter_grade in GRADE_MAP:
        if score >= min_score:
            return letter_grade

    return "F"  # Default grade if no other condition is met
