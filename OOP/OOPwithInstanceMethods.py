# Define the BankAccount class
class BankAccount:
    # Constructor method - Initializes a new instance of BankAccount
    def __init__(self, owner, balance=0):
        self.owner = owner      # Instance variable for the account owner's name
        self.balance = balance  # Instance variable for the account balance, defaults to 0

    # Method - Handles depositing money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Update the balance if the amount is positive
            print(f"Added {amount} to the balance.")
        else:
            print("Invalid amount entered. Please enter a positive number.")

    # Method - Handles withdrawing money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount  # Subtract the amount from balance if sufficient funds
                print(f"Withdrew {amount} from the balance.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount entered. Please enter a positive number.")

    # Method - Returns the current balance of the account
    def check_balance(self):
        return f"The current balance is {self.balance}."

    # Special method - Provides a string representation of the object
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

# This class uses basic concepts like methods, instance variables, and a special method (__str__).
# It demonstrates encapsulation by keeping the balance change logic within the class methods.
