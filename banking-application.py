# Base Class: Account
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        """
        Initializes the Account object with account details.
        :param account_number: Unique identifier for the account
        :param account_holder: Name of the account holder
        :param balance: Initial account balance (default is 0)
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Adds money to the account.
        :param amount: Amount to be deposited
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Withdraws money from the account if sufficient balance is available.
        :param amount: Amount to be withdrawn
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}.")
        else:
            print("Invalid withdrawal amounts. Withdrawal operation cancelled.")

    def display_account_details(self, title="Account Details"):
        """
        Displays the account details.
        :param title: Title to display for the account details
        """
        print(f"\n{title}:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Derived Class: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        """
        Initializes the SavingsAccount object with account details and interest rate.
        :param account_number: Unique identifier for the account
        :param account_holder: Name of the account holder
        :param balance: Initial account balance (default is 0)
        :param interest_rate: Fixed interest rate (default is 2%)
        """
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Calculates and returns the interest based on the current balance and interest rate.
        :return: Calculated interest
        """
        interest = self.balance * self.interest_rate
        print(f"Calculated interest: {interest}")
        return interest

# Demonstration Script
def main():
    """
    Main function to demonstrate the functionality of Account and SavingsAccount classes.
    """
    # Create an instance of SavingsAccount
    account = SavingsAccount(account_number="123456789", account_holder="John Doe", balance=1000, interest_rate=0.03)

    # Display initial account details
    account.display_account_details(title="Account Details (Initial)")
    account.calculate_interest()

    # Perform a deposit
    print("\nPerforming Deposit:")
    deposit_amount = float(input("Enter the amount to deposit: "))
    account.deposit(deposit_amount)
    account.display_account_details(title="Account Details (Updated)")
    account.calculate_interest()

    # Perform a withdrawal
    print("\nPerforming Withdrawal:")
    withdrawal_amount = float(input("Enter the amount to withdraw: "))
    account.withdraw(withdrawal_amount)
    account.display_account_details(title="Account Details (Updated)")
    account.calculate_interest()

# Run the demonstration script
if __name__ == "__main__":
    main()
