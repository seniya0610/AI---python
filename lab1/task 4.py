class BankAccount:
    bankName = "Meezan"

    def __init__(self, name, number, balance):
        self.account_holder = name
        self.account_number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance")

    def display_details(self):
        print(
            f"Bank: {BankAccount.bankName} | Account Holder: {self.account_holder} | Account Number: {self.account_number} | Balance: {self.balance}")


# Example usage
acc1 = BankAccount("Ali", "123456", 5000)

acc1.display_details()
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.withdraw(6000)
