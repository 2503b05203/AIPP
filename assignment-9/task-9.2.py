class SRU_Student:
    # This class represents a student at SRU with basic details
    # and methods to update fees and display the information.

    def __init__(self, name, roll_no, hostel_status):
        # Store the student's name
        self.name = name
        
        # Store the student's roll number
        self.roll_no = roll_no
        
        # Store whether the student is a hosteller or not (Yes/No or True/False)
        self.hostel_status = hostel_status
        
        # Set an initial fee amount (just an example value)
        self.fee = 0

    def fee_update(self, amount):
        # This method updates the student's fee by adding the given amount.
        # We assume the amount is a positive number.
        self.fee += amount

    def display_details(self):
        # This method prints all the details of the student in a readable format.
        print("---- Student Details ----")
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Total Fee Paid: {self.fee}")
        print("-------------------------")


class SRU_Student_AI:
    # AI-generated inline comments for comparison purposes.

    def __init__(self, name, roll_no, hostel_status):
        # AI: Capture the identity details so later methods can refer to them.
        self.name = name
        self.roll_no = roll_no

        # AI: Explicitly note living preference because hostelers often have fee add-ons.
        self.hostel_status = hostel_status

        # AI: Track cumulative fee so subsequent updates can simply add to this bucket.
        self.fee = 0

    def fee_update(self, amount):
        # AI: Incrementally aggregate any new payment into the running total.
        self.fee += amount

    def display_details(self):
        # AI: Present the stored state in a formatted printout for quick verification.
        print("---- Student Details (AI Commented Version) ----")
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Total Fee Paid: {self.fee}")
        print("-----------------------------------------------")



# Main section to test the class
if __name__ == "__main__":
    # Creating an object of SRU_Student with sample values
    student1 = SRU_Student("Rahul Kumar", 12345, "Hosteller")
    
    # Updating the student's fee by adding some amount
    student1.fee_update(50000)
    
    # Displaying the details of the student
    student1.display_details()

    # Creating a second object using the AI-commented class for side-by-side comparison
    student2 = SRU_Student_AI("Priya Sen", 67890, "Day Scholar")
    student2.fee_update(45000)
    student2.display_details()
