#====================================================================
# Script: test_api_client.py
# Descripción: Pruebas del script de geolocalización a través de FreeIPAPI
# Autor: Laura Ramos Granados
# Fecha: 6/2/26
#====================================================================

import unittest, requests
from src.api_client import get_location
from unittest.mock import patch  # Esta es la importación para usar el mock

class ApiClientTest(unittest.TestCase):
    """
        Clase en la cual se ejecutan las pruebras de api_client.py
    """

    """
    Método que evalúa el comportamiento esperado de get_location
    En patch colocamos el módulo que vamos a cambiar y lo que deseamos sobreescribir,
    así crea una variable dentro de la misma prueba que vamos a sustituir 
    """ 
    @patch('src.api_client.requests.get') 
    def test_get_location_expected_data(self, mock_get): # mock_get sustituye a requests.get dentro de api_client
        mock_get.return_value.status_code = 200 # mock_get.return_value representa el objeto response en el api_client
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
            "countryCode": "US"
        } 
        """no son las mismas keys, ni los mismos values que en la app, donde se los estamos dando nosotros.
          Acá se está colocando los valores tal y como nos llegan de internet. Es por eso que se nececitó la traza con ipbd para saber qué estabamos recibiendo."""
        result = get_location("8.8.8.8")
        self.assertEqual(
            # result.get("country"), "United States of America" ----> Antes de aplicar el mock
            result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI") 
        self.assertEqual(result.get("country_code"), "US")
        #luego de aplicar el mock, por un lado tenemos los nombres de las keys que hemos asignado y por otro el resultado que llega directamente del mock, no de intenet
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch('src.api_client.requests.get') 
    def test_get_location_side_effect(self, mock_get): 
        mock_get.side_effect = [ 
            requests.exceptions.RequestException("Service unavailable"),
            unittest.mock.Mock(
                status_code = 200,
                json =lambda: {
                                "countryName": "USA",
                                "regionName": "FLORIDA",
                                "cityName": "MIAMI",
                                "countryCode": "US"
                                }
                            )                   
        ]
        """ Replazado por el unittest.mock
        mock_get.return_value.status_code = 200 
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
            "countryCode": "US"
        } """
        with self.assertRaises(requests.exceptions.RequestException):
            result = get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI") 
        self.assertEqual(result.get("country_code"), "US")
        # mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
        

        #  Reto: Agregar más parámetros a la función get_location y también crear nuevas pruebas. Por ejemplo, agrega el código de país y probar obtener ese valor dentro de una prueba

    @patch('src.api_client.requests.get') 
    def test_get_location_error_status(self, mock_get):
        """
            side_effect define qué pasa cuando llamas al mock.
            Hay 3 usos comunes:
            * devolver valores
            * lanzar excepciones
            * ejecutar una función
        Aquí se usa pra lanzar una excepción:
        """
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_location("8.8.8.8")

    # Reto: Validar si el usuario ha introducido una IP correcta.

