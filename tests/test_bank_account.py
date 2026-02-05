#====================================================================
# Script: tests_bank_account.py 
# Descripción: Tests del script src.bank_account.py
# Autor: Laura Ramos Granados 
# Fecha: 02/02/26
#====================================================================

import unittest, os
from src.bank_account import BankAccount
from src.banxico import api_is_up

BANXICO_TOKEN = os.getenv("BANXICO_TOKEN", "")
class BankAccountTests(unittest.TestCase): 
    """
        Clase heredada de unittest que define las pruebas unitarias para la clase BankAccount
    """

    # El setup, el objeto account que se usa en todas siguientes pruebas
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    # El teardown, borra el archivo después de ejecutar cada prueba
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
        
    # Método que cuenta las líneas del archivo de logs
    def _count_lines_(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

# Testea que el comportamiento del depósito sea el correcto para el valor esperado
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance,1500, "Nuevo balance es incorrecto")

# Testea la respuesta del método deposit cuando el valor es cero
    def test_invalid_amount_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

# Testea que el comportamiento del withdraw sea el correcto para el valor esperado
    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        #assert new_balance == 800
        self.assertEqual(new_balance,800,  "El balance no es correcto")
    
# Testea el comportamiento del retiro cuando el saldo es insuficiente    
    def test_insufficient_funds_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
        with open(self.account.log_file, "r") as f:
            content = f.read()
        self.assertIn('El saldo en su cuenta no es suficiente para realizar este retiro',content)

# Testea la respuesta del método withdraw cuando el valor es cero    
    def test_invalid_amount_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

# Testea la función que muestra el balance
    def test_get_balance(self):
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es correcto")

# Testea que el comportamiento de transfer sea el correcto para el valor esperado
    def test_transfer(self):
        new_balance = self.account.transfer(300)
        self.assertEqual(new_balance, 700, "El balance no es correcto")

# Testea el comportamiento de la transferencia cuando el saldo es insuficiente        
    def test_insufficient_funds_transfer(self):
        with self.assertRaises(ValueError) as e:
            self.account.transfer(1200)        
        with open(self.account.log_file, "r") as f:
            content = f.read()
        self.assertIn("El saldo en su cuenta no es suficiente para realizar esta transferencia", content)

# Testea la respuesta del método transfer cuando el valor es cero    
    def test_invalid_amount_transfer(self):
        with self.assertRaises(ValueError) as e:
            self.account.transfer(0)
        self.assertEqual(str(e.exception), "Importe inválido")

# Testea la existencia del archivo de logs
    def test_transaction_log(self): 
        self.account.get_balance()
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

# Test que checa si el número de líneas en el archivo de logs son correctas
    def test_count_transactions(self):
        assert self._count_lines_(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines_(self.account.log_file) == 2

    @unittest.skipUnless(api_is_up() and BANXICO_TOKEN, "API Banxico no disponible o falta BANXICO_TOKEN")
    def test_convert_mxn_to_usd(self):
        acc = BankAccount(balance=1000, currency="MXN", banxico_token=BANXICO_TOKEN)
        usd = acc.get_balance_usd()
        self.assertGreater(usd, 0)        
    

if __name__== '__main__':
    unittest.main() 