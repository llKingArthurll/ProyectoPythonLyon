import unittest
from miapp.pantalla_formulario import PantallaFormulario

class TestPantallaFormulario(unittest.TestCase):
    def test_obtener_datos(self):
        pantalla = PantallaFormulario()
        pantalla.obtener_datos()
        self.assertNotEqual(pantalla.datos, {})
    
    def test_obtener_datos_guardados(self):
        pantalla = PantallaFormulario()
        pantalla.obtener_datos()
        datos = pantalla.obtener_datos_guardados()
        self.assertNotEqual(datos, {})
        self.assertEqual(datos['nombre'], 'Ejemplo')
        self.assertEqual(datos['edad'], '30')

if __name__ == "__main__":
    unittest.main()
