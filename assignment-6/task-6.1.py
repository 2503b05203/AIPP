class Student:
    """Represents a student with a name, age, and course."""

    def __init__(self, name, age, course):
        """Initializes a new Student object."""
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        """Prints the student's details in a formatted manner."""
        print(f"Student Details:\n  Name: {self.name}\n  Age: {self.age}\n  Course: {self.course}\n")

# Example Usage
student1 = Student("Alice", 20, "Computer Science")
student1.display_details()

student2 = Student("Bob", 22, "Electrical Engineering")
student2.display_details()

student3 = Student("Charlie", 19, "Mechanical Engineering")
student3.display_details()

student4 = Student("Diana", 21, "Physics")
student4.display_details()
