class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# Example Usage
if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.get_balance()
