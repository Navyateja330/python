class Account:
    def __init__(self, balance, accountno):
        self.balance = balance
        self.accountno = accountno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} is debited, balance is {self.getbal()}")
        else:
            print("Insufficient funds")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is credited, balance is {self.getbal()}")

    def getbal(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, interest):
        super().__init__(1000, "acc123") 
        self.interest = interest

    def intereste(self):
        interest_amount = self.balance * (self.interest / 100)
        self.balance += interest_amount
        print(f"Interest added: {interest_amount}, balance is {self.getbal()}")



acc1 = SavingsAccount(5)
acc1.credit(500)
acc1.intereste()
