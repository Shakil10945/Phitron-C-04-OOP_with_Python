class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 1000
        self.max_withdraw = 15000

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount<self.min_withdraw:
            return 'Yet to rech the minimum level'
        elif amount > self.max_withdraw:
            return 'You have crossed the max amount'
        elif amount > self.balance:
            return 'You do not have enough money'
        else :
            self.balance = self.balance -amount
            return "successfully you have  withdraw money"
        
    def deposit(self, amount):
        self. balance = self.balance + amount
        return 'deposited successfully'

my_bank = Bank(9000)
reply = my_bank.withdraw(1600)
print(reply)
print(my_bank.get_balance())
my_bank.deposit(5000)
print(my_bank.get_balance())