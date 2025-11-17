from typing import Union

class SRUStudent:
    """
    Represents a student at SRU with their details and fee information.

    Attributes:
        name (str): The student's name.
        roll_no (Union[str, int]): The student's roll number.
        hostel_status (bool): True if the student is in a hostel, False otherwise.
        fee (float): The student's current fee, initialized to 0.
    """

    def __init__(self, name: str, roll_no: Union[str, int], hostel_status: bool):
        """
        Initializes a new SRUStudent object.

        Args:
            name (str): The student's name.
            roll_no (Union[str, int]): The student's roll number.
            hostel_status (bool): True if the student is in a hostel, False otherwise.
        """
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee = 0.0  # Initialize fee to 0.0

    def fee_update(self, amount: float):
        """
        Updates the student's total fee.

        Args:
            amount (float): The new total fee amount.
        """
        if isinstance(amount, (int, float)) and amount >= 0:
            self.fee = float(amount)
            print(f"\nFee for {self.name} has been updated to: ${self.fee:,.2f}")
        else:
            print("\nError: Invalid fee amount. Please provide a non-negative number.")

    def display_details(self):
        """Prints the student's details in a formatted manner."""
        hostel_info = "Yes" if self.hostel_status else "No"
        print("\n--- Student Details ---")
        print(f"  Name:          {self.name}")
        print(f"  Roll Number:   {self.roll_no}")
        print(f"  Stays in Hostel: {hostel_info}")
        print(f"  Updated Fee:   ${self.fee:,.2f}")
        print("-----------------------")

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Create an instance of the SRUStudent class
    student1 = SRUStudent(name="Subham", roll_no="SRU2024CS101", hostel_status=True)

    # 2. Display the initial details (fee will be 0)
    print("Initial details for the student:")
    student1.display_details()

    # 3. Update the student's fee
    student1.fee_update(55000.50)

    # 4. Display the final details after the fee update
    print("\nFinal details after fee update:")
    student1.display_details()

