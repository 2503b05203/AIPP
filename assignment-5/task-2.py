def evaluate_application(applicant):
    """Evaluates a single loan application based on predefined criteria."""
    # Loan approval criteria
    approved = True
    rejection_reasons = []
 
    if applicant["credit_score"] < 650:
        approved = False
        rejection_reasons.append("Credit score is too low (minimum 650 required).")
 
    if applicant["annual_income"] < 40000:
        approved = False
        rejection_reasons.append("Annual income is too low (minimum $40,000 required).")
 
    if applicant["loan_amount_requested"] > applicant["annual_income"] * 0.5:
        approved = False
        rejection_reasons.append("Loan amount requested exceeds 50% of annual income.")
 
    if applicant["employment_status"] != "Employed":
        approved = False
        rejection_reasons.append("Applicant must be employed.")
 
    if applicant["debt_to_income_ratio"] > 0.40:
        approved = False
        rejection_reasons.append("Debt-to-income ratio is too high (maximum 40%).")
 
    return approved, rejection_reasons

def loan_approval_system():
    print("Welcome to the Loan Approval System!")

    # A list of applicants to test with
    applicants = [
        {
            "name": "John Doe",
            "credit_score": 720,
            "annual_income": 60000,
            "loan_amount_requested": 25000,
            "employment_status": "Employed",
            "debt_to_income_ratio": 0.35,
        },
        {
            "name": "Jane Smith",
            "credit_score": 620,
            "annual_income": 35000,
            "loan_amount_requested": 20000,
            "employment_status": "Unemployed",
            "debt_to_income_ratio": 0.45,
        },
    ]

    for applicant in applicants:
        print(f"\nProcessing loan application for: {applicant['name']}")
        print(f"  Credit Score: {applicant['credit_score']}")
        print(f"  Annual Income: ${applicant['annual_income']:,}")
        print(f"  Loan Amount Requested: ${applicant['loan_amount_requested']:,}")
        print(f"  Employment Status: {applicant['employment_status']}")
        print(f"  Debt-to-Income Ratio: {applicant['debt_to_income_ratio']:.2f}")

        approved, rejection_reasons = evaluate_application(applicant)

        print("\n--- Loan Decision ---")
        if approved:
            print(f"Congratulations, {applicant['name']}! Your loan application for ${applicant['loan_amount_requested']:,} has been APPROVED.")
        else:
            print(f"We regret to inform you, {applicant['name']}, that your loan application has been DENIED.")
            print("Reasons for rejection:")
            for reason in rejection_reasons:
                print(f"- {reason}")

loan_approval_system()