#====================================================================
# Script: tests_all_assert.py 
# Descripción: Clase para probar diferentes tipos de asserts y decorradores 
# Autor: Laura Ramos Granados
# Fecha: 03/02/26
#====================================================================


import unittest 
SERVER = "server_b"

class AllAssertTests(unittest.TestCase):
    """
        Clase para probar los tipos de asserts
    """
    # método assertEqual -> Es igual? 
    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("hola","hola")
    
    # método true -> Es verdadero o falso
    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    # método assert raises -> Expresa este determinado error? 
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no soy un número")

    # método assert in -> El elemento está presente dentro del otro?
    def test_assert_in(self):
        self.assertIn(10, [2, 4, 6, 8, 10])
        self.assertNotIn(10, [2, 4, 6, 8])

    # método assert dict  -> 
    def test_assert_dict(self):
        user = {"first_name":"Laura", "last_name":"Ramos"}
        self.assertDictEqual(
            {"first_name":"Laura", "last_name":"Ramos"}, 
            user
        )
    
    # lo mismo para sets -> assertSetEqual

    # Pasar una prueba aunque esté presente, solo pasar de ella, porque esté en construcción u otros 
    @unittest.skip("Trabajo en progreso. Será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola","chao")

    # @unittest.skipIf(True, "Saltada porque no estamos en el servidor"). Arriba se define la variable SERVER con un servidor diferente (server_b) para que así se salte la prueba, ya que la condición no es verdadera
    @unittest.skipIf(SERVER == "server_b", "Saltada porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100,100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)

"""
    Reto: Imagina que nuestra app de banco va a empezar a utilizar varias monedas y que se conecta a una API para obtener el valor del cambio, utilizando skipunless para que pueda validar si la API está corriendo y después de que esté corriendo ejecutar las validaciones, trayendo el precio del dólar y modificando la clase del BankAccount para ver como se pueden manejar dos currencies dentro de la misma clase 
"""