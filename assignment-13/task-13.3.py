class Student:
    """Represents a student with their name, age, and marks."""

    def __init__(self, name: str, age: int, *marks: float):
        """
        Initializes a Student object.

        Args:
            name (str): The full name of the student.
            age (int): The age of the student.
            *marks (float): A variable number of marks for the student's subjects.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self) -> str:
        """Returns a user-friendly string representation of the student's details."""
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self) -> str:
        """Returns an unambiguous string representation of the student object."""
        return f"Student(name='{self.name}', age={self.age}, marks={self.marks})"

    def calculate_total_marks(self) -> float:
        """Calculates and returns the sum of all marks for the student."""
        return sum(self.marks)

    def display_summary(self):
        """Prints a formatted summary of the student's details and total marks."""
        print(self)  # This calls the __str__ method
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.calculate_total_marks()}")


if __name__ == "__main__":
    # Example usage of the refactored Student class

    # Create a student with 3 marks
    student1 = Student("Alice", 20, 85, 90, 78)
    print("--- Student 1 Summary ---")
    student1.display_summary()
    print("\nObject representation:", repr(student1))

    print("-" * 25)

    # Create another student with 5 marks, demonstrating flexibility
    student2 = Student("Bob", 22, 92.5, 88, 95, 89, 91)
    print("--- Student 2 Summary ---")
    student2.display_summary()
    print("\nObject representation:", repr(student2))
