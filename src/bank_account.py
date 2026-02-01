
# Clase que define una cuenta bancaria
class BankAccount: 
    # método constructor
    def __init__(self, balance=0):
        self.balance = balance
    
    # método depósito 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    # método retiro
    def withdraw(self, amount):
        if amount > 0: 
            self.balance -= amount
        return self.balance
    
    # getter balance
    def get_balance(self): 
        return self.balance