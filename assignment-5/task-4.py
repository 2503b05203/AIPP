def calculate_applicant_score(applicant):
    """
    Calculates a score for a job applicant based on predefined criteria.

    Args:
        applicant (dict): A dictionary containing applicant's information with keys like
                          'experience_years', 'education_level', 'skills', 'has_certifications'.

    Returns:
        int: The total score for the applicant.
    """
    score = 0

    # Experience:
    # 0-1 year: 5 points
    # 2-4 years: 10 points
    # 5+ years: 15 points
    if applicant["experience_years"] >= 5:
        score += 15
    elif applicant["experience_years"] >= 2:
        score += 10
    elif applicant["experience_years"] >= 0:
        score += 5

    # Education Level:
    # High School: 5 points
    # Bachelor's: 10 points
    # Master's/PhD: 15 points
    education_level = applicant["education_level"].lower()
    if education_level == "master's" or education_level == "phd":
        score += 15
    elif education_level == "bachelor's":
        score += 10
    elif education_level == "high school":
        score += 5

    # Skills:
    # Each relevant skill adds 3 points
    relevant_skills = ["python", "java", "sql", "cloud", "machine learning"]
    for skill in applicant["skills"]:
        if skill.lower() in relevant_skills:
            score += 3

    # Certifications:
    # Adds 5 points if applicant has certifications
    if applicant["has_certifications"]:
        score += 5

    return score

def job_applicant_scoring_system():
    """
    Simulates a job applicant scoring system.
    """
    print("Welcome to the Job Applicant Scoring System!")

    applicants = [
        {
            "name": "Alice Johnson",
            "experience_years": 3,
            "education_level": "Bachelor's", 
            "skills": ["Python", "SQL", "Data Analysis"],
            "has_certifications": True,
        },
        {
            "name": "Bob Williams",
            "experience_years": 7,
            "education_level": "Master's",
            "skills": ["Java", "Cloud", "DevOps"],
            "has_certifications": True,
        },
        {
            "name": "Charlie Brown",
            "experience_years": 1,
            "education_level": "High School",
            "skills": ["Customer Service", "Sales"],
            "has_certifications": False,
        },
        {
            "name": "Diana Prince",
            "experience_years": 4,
            "education_level": "Bachelor's",
            "skills": ["Machine Learning", "Python", "Statistics"],
            "has_certifications": True,
        },
    ]

    for applicant in applicants:
        score = calculate_applicant_score(applicant)
        print(f"\nApplicant: {applicant['name']}")
        print(f"  Score: {score}")

if __name__ == "__main__":
    job_applicant_scoring_system()