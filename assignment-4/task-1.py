def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND not divisible by 100, OR
    - It is divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


# Test cases
if __name__ == "__main__":
    test_years = [2000, 1900, 2020, 2021, 2024]
    for year in test_years:
        print(f"{year}: {is_leap_year(year)}")