def classify_person_by_age(age):
    """
    Classifies a person based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        str: A string indicating the age classification (e.g., "Child", "Teenager", "Adult", "Senior").
    """
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 64:
        return "Adult"
    else:
        return "Senior"

# Example Usage
print(f"Age 10: {classify_person_by_age(10)}")
print(f"Age 15: {classify_person_by_age(15)}")
print(f"Age 30: {classify_person_by_age(30)}")
print(f"Age 70: {classify_person_by_age(70)}")
