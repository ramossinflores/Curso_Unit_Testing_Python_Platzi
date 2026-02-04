#====================================================================
# Script: bank_account.py
# Descripción: Clase com métodos básicos de acciones en una cuenta banacaria
# Autor: Laura Ramos Granados
# Fecha 02/02/26
#====================================================================

from src.banxico import get_usd_mxn_fix


# Clase que representa una cuenta bancaria
class BankAccount: 
    # método constructor, determina el balance, con valor por defecto 0
    # se añade el parámetro log_file para instanciar un nuevo archivo de logs cada vez que se crea una instancia
    
    def __init__(self, balance=0,  currency="MXN", log_file=None, banxico_token=None):
        self.balance = balance
        self.log_file = log_file
        self.currency= currency
        self.banxico_token = banxico_token
        self._log_transaction('Cuenta creada')

    def get_balance_usd(self):
            """
            Si la cuenta está en MXN, convierte a USD usando FIX (MXN por USD).
            USD = MXN / (MXN por USD)
            """
            if self.currency == "USD":
                return float(self.balance)
            if self.currency != "MXN":
                raise ValueError("Solo soportado MXN->USD en este reto")

            if not self.banxico_token:
                raise ValueError("Falta banxico_token")

            mxn_per_usd = get_usd_mxn_fix(self.banxico_token)
            return float(self.balance) / mxn_per_usd


    # Helper que agrega un log en archivo cada vez que hay una transacción
    def _log_transaction(self, message): 
        if self.log_file: 
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"{message}\n")
    
    # método depósito
    def deposit(self, amount):
        if amount <= 0: # primero, comprueba si el valor es menor o igual a cero
            self._log_transaction('Operación fallida: Importe inválido')
            raise ValueError('Importe inválido')
        self.balance += amount # si no es así, sumo cantidad al balance
        self._log_transaction(f'Depositado: {amount}. Nuevo balance: {self.balance}')
        return self.balance
    
    # método retiro
    def withdraw(self, amount):
        if amount <= 0: # primero, comprueba si el valor es menor o igual a cero
            self._log_transaction('Operación fallida: Importe inválido')
            raise ValueError('Importe inválido')
        if amount > self.balance: # segundo, se asegura que la cantidad no sea mayor que el balance, que no haya un sobre giro
            self._log_transaction(f'El saldo en su cuenta no es suficiente para realizar este retiro')
            raise ValueError('Operación fallida: Saldo insuficiente ')
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
            self._log_transaction('Operación fallida: Importe inválido')
            raise ValueError('Importe inválido')        
        if amount > self.balance: # segundo, se asegura que la cantidad no sea mayor que el balance, muestra la cantidad que no puede tranferir en contraste con el saldo actual
            self._log_transaction('El saldo en su cuenta no es suficiente para realizar esta transferencia')
            raise ValueError(f'No es posible transferir {amount}. Saldo disponible: {self.balance}.')
        self.balance -= amount
        self._log_transaction(f'Transferido: {amount}. Nuevo balance: {self.balance}')
        return self.balance
    
