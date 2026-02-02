#====================================================================
# Script: test_calculator.py
# Descripción: Tests unitarios para el script src.calculator.py
# Autor: Laura Ramos Granados
# Fecha 02/02/26
#====================================================================


import unittest
from src.calculator import add, subtract, multiply, divide

# Paso 1. Crear una clase que hereda de Unit Test
class CalculatorTest(unittest.TestCase):
    """
        Esta clase se hereda de Unit Test y nos permite ver el progreso de las pruebas, qué prueba se ejecutó, qué prueba falló, por qué falló
    """
    def test_add(self):
        # assert sum(2,3) == 5
        self.assertEqual(add(2,3),5)
    
    def test_subtract(self):
        #assert substract(10,5) == 5
        self.assertEqual(subtract(7,3), 4)
    
    def test_multiply(self):
        # assert multiply(3,5) == 15
        self.assertEqual(multiply(2,3),6)

    def test_divide(self):
        # assert divide(10,5) == 2    
        self.assertEqual(divide(10,2), 5)

    def test_divide_by_zero(self):
        """
            result = divide(10,2)
            expected = 5
            assert result == expected 
        """
        
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)

if __name__ == "__main__":
    unittest.main()