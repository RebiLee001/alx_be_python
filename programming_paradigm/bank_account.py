class BankAccount:
    """A simple bank account class that supports deposit, withdrawal, and balance display."""

    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print current balance with two decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
