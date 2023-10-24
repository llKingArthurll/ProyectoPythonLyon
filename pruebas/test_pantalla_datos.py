import unittest
from miapp.pantalla_datos import PantallaDatos

class TestPantallaDatos(unittest.TestCase):
    def test_mostrar_datos(self):
        datos = {'nombre': 'Ejemplo', 'edad': '30'}
        pantalla = PantallaDatos(datos)
        with unittest.mock.patch('builtins.print') as mock_print:
            pantalla.mostrar_datos()
            mock_print.assert_called_with("Nombre: Ejemplo")
            mock_print.assert_called_with("Edad: 30")

if __name__ == "__main__":
    unittest.main()
