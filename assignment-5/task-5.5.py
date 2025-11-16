def decide_title(name, gender):
    """
    Decides the title (Mr. or Ms.) based on the specified gender.
    
    Args:
        name (str): The applicant's name.
        gender (str): The applicant's gender ('Male' or 'Female').
        
    Returns:
        str: A formal greeting including the name and title.
    """
    # Normalize gender input to handle minor case variations
    gender_lower = gender.lower()
    
    if gender_lower == 'male':
        title = "Mr."
    elif gender_lower == 'female':
        title = "Ms." # Ms. is generally used as a default for formal neutrality
    else:
        # Fallback for unexpected or missing gender data
        return f"Welcome, {name}. We're ready for your interview."
        
    return f"Good morning, {title} {name}. Please proceed to the interview room."


def process_applicants(applicants_data):
    """Processes mock applicant data and prints a formal greeting with title."""
    print("--- Applicant Greeting Output ---")
    
    for applicant in applicants_data:
        name = applicant['name']
        gender = applicant['gender']
        
        greeting = decide_title(name, gender)
        print(f"**{name}** ({gender}): {greeting}")


# --- Mock Data ---
# Note: This dictionary simulates a database or file input where gender is pre-recorded.
applicant_mock_data = [
    {"name": "Elias Vance", "gender": "Male"},
    {"name": "Sophia Chen", "gender": "Female"},
    {"name": "Markus Zeller", "gender": "Male"},
    {"name": "Olivia Reed", "gender": "Female"},
    {"name": "Jordan Casey", "gender": "Other"} # Demonstrates the fallback
]


if __name__ == "__main__":
    process_applicants(applicant_mock_data)