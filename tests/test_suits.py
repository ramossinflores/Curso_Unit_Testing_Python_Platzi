#====================================================================
# Script: test_suits.py
# Descripción: Implementar suits
# Autor: Laura Ramos Granados
# Fecha 04/02/26
#====================================================================

import unittest
from tests.test_bank_account import BankAccountTests

def bank_account_suite():
    suite = unittest.TestSuite() # Crea una suit 
    suite.addTest(BankAccountTests("test_deposit")) # y además agrega estas pruebas
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite 

if __name__ == "__main__": 
    runner = unittest.TextTestRunner() # Se crea un runner para correr las pruebas
    runner.run(bank_account_suite())

# PYTHONPATH=. python .\tests\tests_suits.py ----> en Linux
# $env:PYTHONPATH="." ----> En PowerShell
# python .\tests\tests_suits.py

