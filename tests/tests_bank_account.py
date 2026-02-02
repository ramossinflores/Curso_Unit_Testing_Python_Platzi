import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase): 

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance,1500)

    def test_invalid_amount_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        #assert new_balance == 800
        self.assertEqual(new_balance,800)
    
    def test_insufficient_funds_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
    
    def test_invalid_amount_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_get_balance(self):
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer(self):
        new_balance = self.account.transfer(300)
        self.assertEqual(new_balance, 700)
    
    def test_insufficient_funds_transfer(self):
        with self.assertRaises(ValueError):
            self.account.transfer(1200)

    def test_invalid_amount_transfer(self):
        with self.assertRaises(ValueError):
            self.account.transfer(0)

if __name__== '__main__':
    unittest.main()