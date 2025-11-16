def cm_to_inches(centimeters):
    """Convert centimeters to inches."""
    inches = centimeters / 2.54
    return round(inches, 2)

# Get user input
user_input = float(input("Enter centimeters: "))
result = cm_to_inches(user_input)
print(f"{user_input} cm = {result} inches")