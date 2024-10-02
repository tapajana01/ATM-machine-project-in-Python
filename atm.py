# ATM Machine Simulation

import getpass
import sys
from datetime import datetime

class ATM:
    def __init__(self, account_number, pin, balance=0):
        """
        Initialize the ATM with account details.
        
        :param account_number: The user's account number
        :param pin: The user's PIN
        :param balance: The starting balance (default is 0)
        """
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self):
        """
        Prompt the user to enter their PIN and verify it.
        
        :return: True if PIN is correct, False otherwise
        """
        attempts = 3
        while attempts > 0:
            entered_pin = getpass.getpass("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts remaining: {attempts}")
        print("Too many incorrect attempts. Exiting.")
        return False

    def display_menu(self):
        """
        Display the ATM menu options.
        """
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")

    def balance_inquiry(self):
        """
        Display the current account balance.
        """
        print(f"Your current balance is: ${self.balance:.2f}")

    def cash_withdrawal(self):
        """
        Allow the user to withdraw cash from their account.
        """
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(
                f"{datetime.now()}: Withdrawn ${amount:.2f}"
            )
            print(f"Please take your cash: ${amount:.2f}")
            print(f"New balance: ${self.balance:.2f}")

    def cash_deposit(self):
        """
        Allow the user to deposit cash into their account.
        """
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            self.transaction_history.append(
                f"{datetime.now()}: Deposited ${amount:.2f}"
            )
            print(f"${amount:.2f} deposited successfully.")
            print(f"New balance: ${self.balance:.2f}")

    def pin_change(self):
        """
        Allow the user to change their PIN.
        """
        current_pin = getpass.getpass("Enter current PIN: ")
        if current_pin != self.pin:
            print("Incorrect current PIN.")
            return
        new_pin = getpass.getpass("Enter new PIN: ")
        confirm_pin = getpass.getpass("Confirm new PIN: ")
        if new_pin != confirm_pin:
            print("PINs do not match. PIN change failed.")
        elif not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be a 4-digit number.")
        else:
            self.pin = new_pin
            print("PIN changed successfully.")

    def transaction_history_display(self):
        """
        Display the user's transaction history.
        """
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("\n--- Transaction History ---")
            for transaction in self.transaction_history:
                print(transaction)

    def run(self):
        """
        Run the ATM simulation.
        """
        print("Welcome to the ATM Machine Simulation!")
        if not self.verify_pin():
            sys.exit()

        while True:
            self.display_menu()
            choice = input("Select an option (1-6): ")

            if choice == '1':
                self.balance_inquiry()
            elif choice == '2':
                self.cash_withdrawal()
            elif choice == '3':
                self.cash_deposit()
            elif choice == '4':
                self.pin_change()
            elif choice == '5':
                self.transaction_history_display()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose a valid option.")

def main():
    """
    Main function to initialize the ATM and start the simulation.
    """
    # For simulation purposes, we set a default account number and PIN
    account_number = "123456789"
    pin = "1234"
    initial_balance = 1000.00  # Starting with $1000

    # Create an instance of the ATM class
    atm = ATM(account_number, pin, initial_balance)

    # Run the ATM simulation
    atm.run()

if __name__ == "__main__":
    main()
