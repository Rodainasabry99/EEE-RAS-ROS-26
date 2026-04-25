class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")



acc = BankAccount()

acc.deposit(100)
acc.withdraw(30)
acc.withdraw(100)

print("Current Balance:", acc.balance)