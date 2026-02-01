
# Clase que define una cuenta bancaria
class BankAccount: 
    # método constructor
    def __init__(self, balance=0):
        self.balance = balance
    
    # método depósito 
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('El depósito debe ser mayor y distinto de 0')
        self.balance += amount
        return self.balance
    
    # método retiro
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('El retiro debe ser mayor y distinto de 0')
        if amount > self.balance:
            raise ValueError('El saldo en su cuenta no es suficiente para realizar este retiro')
        self.balance -= amount
        return self.balance
    
    # getter balance
    def get_balance(self): 
        return self.balance
    
    # método transferencia
    def transfer(self, amount):
        if amount < self.balance: 
            raise ValueError(f'No es posible transferir {amount}. Saldo disponible: {self.balance}.')
        if amount <=0:
            raise ValueError('La cantidad debe ser mayor y distinta de cero')
        self.balance -= amount