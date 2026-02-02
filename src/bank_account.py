#====================================================================
# Script: bank_account.py
# Descripción: Clase com métodos básicos de acciones en una cuenta banacaria
# Autor: Laura Ramos Granados
# Fecha 02/02/26
#====================================================================

# Clase que representa una cuenta bancaria
class BankAccount: 
    # método constructor, determina el balance, con valor por defecto 0
    def __init__(self, balance=0):
        self.balance = balance
    
    # método depósito
    def deposit(self, amount):
        if amount <= 0: # primero, comprueba si el valor es menor o igual a cero
            raise ValueError('La cantidad debe ser mayor que 0')
        self.balance += amount # si no es así, sumo cantidad al balance
        return self.balance
    
    # método retiro
    def withdraw(self, amount):
        if amount <= 0: # primero, comprueba si el valor es menor o igual a cero
            raise ValueError('La cantidad debe ser mayor que 0')
        if amount > self.balance: # segundo, se asegura que la cantidad no sea mayor que el balance, que no haya un sobre giro
            raise ValueError('El saldo en su cuenta no es suficiente para realizar este retiro')
        self.balance -= amount # terccero, si las condiciones anteriores no se cumplen, resto la cantidad al balance
        return self.balance
    
    # getter balance
    def get_balance(self): 
        return self.balance
    
    # método transferencia
    def transfer(self, amount):
        if amount <=0:  # primero, comprueba si el valor es menor o igual a cero
            raise ValueError('La cantidad debe ser mayor que 0')        
        if amount > self.balance: # segundo, se asegura que la cantidad no sea mayor que el balance, muestra la cantidad que no puede tranferir en contraste con el saldo actual
            raise ValueError(f'No es posible transferir {amount}. Saldo disponible: {self.balance}.')
        self.balance -= amount
        return self.balance
    