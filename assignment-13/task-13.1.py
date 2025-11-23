import math

def _calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

def _calculate_square_area(side):
    """Calculates the area of a square."""
    return side * side

def _calculate_circle_area(radius):
    """Calculates the area of a circle."""
    return math.pi * radius * radius

# A dispatch table to map shape names to their area functions.
# This makes the code easily extendable. To add a new shape,
# you just need to add a new function and an entry to this dictionary.
_SHAPE_CALCULATORS = {
    "rectangle": (_calculate_rectangle_area, 2), # function and expected number of arguments
    "square": (_calculate_square_area, 1),
    "circle": (_calculate_circle_area, 1),
}

def calculate_area(shape, *args):
    """
    Calculates the area of a given shape using a dispatch table.

    Args:
        shape (str): The name of the shape (e.g., "rectangle", "square", "circle").
        *args: The dimensions of the shape.
               - rectangle: (length, width)
               - square: (side)
               - circle: (radius)

    Returns:
        float: The calculated area of the shape.
    """
    if shape not in _SHAPE_CALCULATORS:
        raise ValueError(f"Unknown shape: '{shape}'. Supported shapes are: {list(_SHAPE_CALCULATORS.keys())}")

    calculator_func, num_args = _SHAPE_CALCULATORS[shape]
    if len(args) != num_args:
        raise TypeError(f"Invalid number of arguments for {shape}. Expected {num_args}, got {len(args)}.")
    
    return calculator_func(*args)


# Rectangle with length 5 and width 10
print("rectangle area:", calculate_area("rectangle", 5, 10))  # Output: 50

# Square with side 4
print("square area:", calculate_area("square", 4))         # Output: 16

# Circle with radius 3
print("circle area:", calculate_area("circle", 3))         # Output: 28.274333882308138