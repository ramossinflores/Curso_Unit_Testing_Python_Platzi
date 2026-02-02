#====================================================================
# Script: bank_account.py
# Descripción: Clase com métodos básicos de acciones en una cuenta banacaria
# Autor: Laura Ramos Granados
# Fecha 02/02/26
#====================================================================

# Clase que representa una cuenta bancaria
class BankAccount: 
    # método constructor, determina el balance, con valor por defecto 0
    # se añade el parámetro log_file para instanciar un nuevo archivo de logs cada vez que se crea una instancia
    def __init__(self, balance=0, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    # Helper que agrega un log en archivo cada vez que hay una transacción
    def _log_transaction(self, message): 
        if self.log_file: 
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"{message}\n")
    
    # método depósito
    def deposit(self, amount):
        if amount <= 0: # primero, comprueba si el valor es menor o igual a cero
            raise ValueError('La cantidad debe ser mayor que 0')
        self.balance += amount # si no es así, sumo cantidad al balance
        self._log_transaction(f'Depositado: {amount}. Nuevo balance: {self.balance}')
        return self.balance
    
    # método retiro
    def withdraw(self, amount):
        if amount <= 0: # primero, comprueba si el valor es menor o igual a cero
            raise ValueError('La cantidad debe ser mayor que 0')
        if amount > self.balance: # segundo, se asegura que la cantidad no sea mayor que el balance, que no haya un sobre giro
            raise ValueError('El saldo en su cuenta no es suficiente para realizar este retiro')
        self.balance -= amount # tercero, si las condiciones anteriores no se cumplen, resto la cantidad al balance
        self._log_transaction(f'Retirado: {amount}. Nuevo balance: {self.balance}')
        return self.balance
    
    # getter balance
    def get_balance(self): 
        self._log_transaction(f'Revisó el balance. Balance actual: {self.balance}')
        return self.balance
    
    # método transferencia
    def transfer(self, amount):
        if amount <=0:  # primero, comprueba si el valor es menor o igual a cero
            raise ValueError('La cantidad debe ser mayor que 0')        
        if amount > self.balance: # segundo, se asegura que la cantidad no sea mayor que el balance, muestra la cantidad que no puede tranferir en contraste con el saldo actual
            raise ValueError(f'No es posible transferir {amount}. Saldo disponible: {self.balance}.')
        self.balance -= amount
        self._log_transaction(f'Transferido: {amount}. Nuevo balance: {self.balance}')
        return self.balance
    
    # agrega un logh cada vez que alguien haga un transferencia y no tenga saldo disponible, texto que diga que no tiene slado disponible