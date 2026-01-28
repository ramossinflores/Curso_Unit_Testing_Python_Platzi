import unittest
from src.calculator import sum, substract

# Paso 1. Crear una clase que hereda de Unit Test
class CalculatorTest(unittest.TestCase):
    """
        Esta clase se hereda de Unit Test y nos permite ver el progreso de las pruebas, qué prueba se ejecutó, qué prueba falló, por qué falló
    """
    def test_sum(self):
        assert sum(2,3) == 5
    
    def test_substract(self):
        assert substract(10,5) == 5