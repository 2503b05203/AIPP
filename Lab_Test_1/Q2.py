
"""
    This class represents a rectangle using its width and height.
    
    It can tell you two things:
    - area of the rectangle
    - perimeter of the rectangle
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


class RectangleAIDocs:
    """
    AI-generated: Encapsulates a rectangle and exposes analytical helpers.

    Attributes:
        width (float): Positive horizontal extent in arbitrary units.
        height (float): Positive vertical extent matched to the width units.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        AI-generated: Initialize the rectangle, validating the provided bounds.

        Args:
            width: Measured span along the x-axis; must exceed zero.
            height: Measured span along the y-axis; must exceed zero.

        Raises:
            ValueError: If either dimension is non-positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError(
                "RectangleAIDocs expects strictly positive width and height."
            )

        # Persist the sanitized dimensions for downstream geometric formulas.
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        AI-generated: Compute the enclosed two-dimensional measure.

        Returns:
            float: Product of width and height, representing surface coverage.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        AI-generated: Compute the total boundary length.

        Returns:
            float: Twice the sum of width and height, i.e., 2*(w + h).
        """
        # Boundary length equals adding paired edges and doubling them.
        return 2 * (self.width + self.height)





if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print("Manual Rectangle:")
    print(rect.area())
    print(rect.perimeter())

    rect_ai = RectangleAIDocs(5, 3)
    print("AI-documented Rectangle:")
    print(rect_ai.area())
    print(rect_ai.perimeter())
