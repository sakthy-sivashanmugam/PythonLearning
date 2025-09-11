class BankAccount:
    def __init__(self, account_holder, balance=0.0, account_type='Any'):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance")
   

    def display_balance(self):
            print(f"Account Holder:{self.account_holder},Account Type: {self.account_type}, Balance: ${self.balance:.2f}")

    
account1 = BankAccount("Sakthy", 1000.0, "Savings")
account2 = BankAccount("Babu", 500.0, "Current")

account1.display_balance()
account1.deposit(200)
account1.withdraw(150)
account1.display_balance()

account2.display_balance()
account2.withdraw(600)
account2.deposit(300)
account2.display_balance()

