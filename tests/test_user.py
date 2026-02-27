import unittest, os
from faker import Faker  # Importación de la librería Faker 
from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):
    def setUp(self):
        """Levantamos un setup para todas las pruebas, objeto generador con el parámetro local en español """
        self.faker = Faker(locale="es") 
        self.user = User(self.faker.name(), self.faker.email())
    
    def test_user_creation(self):
        """
            Prueba para la generación de un usuario 
        """
        name_generated = self.faker.name() # nombre generado aleatoriamente 
        email_generated = self.faker.email()  # nombre generado aleatoriamente 
        user = User(name_generated,email_generated)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
        
    def test_user_with_multiple_accounts(self):
        for _ in range(3): # Agrega 3 cuentas al usuario generado 
            bank_account = BankAccount( # instancia el objeto cuenta bancaria y se rellena con información fake
                balance = self.faker.random_int(min=100, max=1000, step=50), # Creación de balance de la cuenta fake
                log_file= self.faker.file_name(extension=".txt") # Nombre de archivo generado
            )
            self.user.add_account(bank_account)

        expected_value = self.user.get_total_balance() 
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value,expected_value)

    def tearDown(self):
        for account in self.user.accounts:
            os.remove(account.log_file)