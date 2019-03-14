class BankAccount(object):
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        if(self.balance == 'closed'):
            raise ValueError('ValueError')
        return self.balance

    def open(self):
        self.balance = 0

    def deposit(self, amount):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('ValueError')
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('ValueError')
        self.balance = self.balance - amount

    def close(self):
        self.balance = "closed"

    
    def __str__(self): 
        return 'Balance on account: $' + str(self.balance)

   
myAccount = BankAccount() # Make instance of BankAccount

myAccount.deposit(500)
myAccount.withdraw(50)
print("Dan's " + str(myAccount))