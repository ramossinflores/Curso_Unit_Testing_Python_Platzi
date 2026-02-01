import unittest
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase): 
    def test_deposit(self):
        account = BankAccount(balance=1000)
        new_balance = account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        account = BankAccount(balance=1000)
        new_balance = account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):
        account = BankAccount(balance=1000)
        assert account.get_balance() == 1000