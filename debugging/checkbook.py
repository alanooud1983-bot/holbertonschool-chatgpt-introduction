#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.
        
        Parameters:
        amount (float): The amount to deposit
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.
        
        Parameters:
        amount (float): The amount to withdraw
        
        Returns:
        bool: True if withdrawal successful, False otherwise
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return False
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
            return True

    def get_balance(self):
        """
        Display the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            
            if action == 'exit':
                print("Goodbye!")
                break
            elif action == 'deposit':
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                except ValueError:
                    print("Error: Please enter a valid number for the deposit amount.")
            elif action == 'withdraw':
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                except ValueError:
                    print("Error: Please enter a valid number for the withdrawal amount.")
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please choose from: deposit, withdraw, balance, exit")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
