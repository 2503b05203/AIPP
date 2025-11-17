class BankAccount:
    """Represents a simple bank account."""

    def __init__(self, account_number, initial_balance=0):
        """
        Initializes a new BankAccount object.

        Args:
            account_number (str): The unique account number.
            initial_balance (float): The initial balance of the account. Defaults to 0.
        """
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """
        Prints the current balance of the account.
        """
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")

# Example Usage
my_account = BankAccount("123456789", 1000)
my_account.check_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500)  # Insufficient funds
my_account.deposit(-100)  # Invalid deposit
my_account.check_balance()

another_account = BankAccount("987654321")
another_account.check_balance()
another_account.deposit(250.75)
another_account.withdraw