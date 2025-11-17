class Employee:
    """
    Represents an employee with a name and salary information.

    Attributes:
        _name (str): The employee's name (intended for internal use).
        _salary (float): The employee's current salary (intended for internal use).
    """

    def __init__(self, name: str, salary: float):
        """
        Initializes a new Employee object.

        Args:
            name (str): The full name of the employee.
            salary (float): The initial salary of the employee.
        """
        self._name = name
        self._salary = float(salary)

    def increase_salary(self, percentage: float):
        """
        Increases the employee's salary by a given percentage.

        Args:
            percentage (float): The percentage to increase the salary by.
                                Must be a non-negative number.
        """
        if percentage < 0:
            print("Error: Percentage increase cannot be negative.")
            return

        self._salary *= (1 + percentage / 100)
        print(f"\nSalary for {self._name} increased by {percentage}%.")

    def display_info(self):
        """Prints the employee's details in a formatted manner."""
        print("\n--- Employee Information ---")
        print(f"  Name:   {self._name}")
        print(f"  Salary: ${self._salary:,.2f}")
        print("--------------------------")


# --- Example Usage ---
if __name__ == "__main__":
    # Create an instance of the Employee class
    emp1 = Employee("John Doe", 70000)

    # Display initial information
    emp1.display_info()

    # Increase the employee's salary
    emp1.increase_salary(10)

    # Display the updated information
    emp1.display_info()
