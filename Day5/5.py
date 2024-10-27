class Bank:
    def __init__(self, acno, name, balance=0):
        self.acno = acno
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")

    def enquiry(self):
        print(f"Available balance: ₹{self.balance}")

account = Bank(123456, "Alice", 1000)

account.deposit(500)

account.withdraw(200)

account.enquiry()
