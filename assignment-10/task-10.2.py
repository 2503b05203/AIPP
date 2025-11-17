from typing import List, Any

def find_common(a: List[Any], b: List[Any]) -> List[Any]:
    """Return a list of common elements between two lists a and b."""
    # Convert lists to sets, find the intersection, and convert back to a list.
    return list(set(a) & set(b))

# Example usage to demonstrate the function
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 5]
    list2 = [4, 5, 6, 7, 8, 5]
    
    common_elements = find_common(list1, list2)
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Common elements: {common_elements}")
