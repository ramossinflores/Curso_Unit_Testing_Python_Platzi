#====================================================================
# Script: tests_bank_account.py 
# Descripción: Tests del script src.bank_account.py
# Autor: Laura Ramos Granados 
# Fecha: 02/02/26
#====================================================================

import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase): 
    """
        Clase heredada de unittest que define las pruebas unitarias para la clase BankAccount
    """

    # El setup, el objeto account que se usa en todas siguientes pruebas
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

# Testea que el comportamiento del depósito sea el correcto para el valor esperado
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance,1500)

# Testea la respuesta del método deposit cuando el valor es cero
    def test_invalid_amount_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

# Testea que el comportamiento del withdraw sea el correcto para el valor esperado
    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        #assert new_balance == 800
        self.assertEqual(new_balance,800)
    
# Testea el comportamiento del retiro cuando el saldo es insuficiente    
    def test_insufficient_funds_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

# Testea la respuesta del método withdraw cuando el valor es cero    
    def test_invalid_amount_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

# Testea la función que muestra el balance
    def test_get_balance(self):
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000)

# Testea que el comportamiento de transfer sea el correcto para el valor esperado
    def test_transfer(self):
        new_balance = self.account.transfer(300)
        self.assertEqual(new_balance, 700)

# Testea el comportamiento de la transferencia cuando el saldo es insuficiente        
    def test_insufficient_funds_transfer(self):
        with self.assertRaises(ValueError):
            self.account.transfer(1200)

# Testea la respuesta del método transfer cuando el valor es cero    
    def test_invalid_amount_transfer(self):
        with self.assertRaises(ValueError):
            self.account.transfer(0)

if __name__== '__main__':
    unittest.main()