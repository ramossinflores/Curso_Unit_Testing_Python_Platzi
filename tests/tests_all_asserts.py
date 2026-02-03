import unittest 

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