# Example 1: Simple function with string split
def format_name(full_name):
    """Formats 'First Last' to 'Last, First'"""
    parts = full_name.strip().split()
    if len(parts) >= 2:
        return f"{parts[-1]}, {parts[0]}"
    return full_name

# Example 2: Using rsplit for better handling of middle names
def format_name_v2(full_name):
    """Formats name with middle names: 'First Middle Last' to 'Last, First Middle'"""
    parts = full_name.strip().rsplit(maxsplit=1)
    if len(parts) == 2:
        return f"{parts[1]}, {parts[0]}"
    return full_name

# Example 3: More robust with error handling
def format_name_v3(full_name):
    """Formats name with validation"""
    if not full_name or not isinstance(full_name, str):
        return None
    
    parts = full_name.strip().split()
    if len(parts) < 2:
        return None
    
    first = parts[0]
    last = parts[-1]
    middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""
    
    return f"{last}, {first}" + (f" {middle}" if middle else "")

# Test cases
print(format_name("John Smith"))  # Smith, John
print(format_name_v2("John Michael Smith"))  # Smith, John Michael
print(format_name_v3("Jane Marie Doe"))  # Doe, Jane Marie