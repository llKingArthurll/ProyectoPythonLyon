from miapp.view.pantalla_bienvenida import PantallaBienvenida
from miapp.view.pantalla_opciones import PantallaOpciones
from miapp.view.pantalla_formulario import PantallaFormulario
from miapp.view.pantalla_agregar_productos import PantallaAgregarProductos
from miapp.view.pantalla_agregar_series import PantallaAgregarSeries
from miapp.view.pantalla_resumen import PantallaResumen
from miapp.model.datos_model import DatosModel

class PantallaController:
    def __init__(self, root):
        self.root = root
        self.model = DatosModel()
        self.bienvenida = PantallaBienvenida(root)
        self.opciones = PantallaOpciones(root)
        self.formulario = PantallaFormulario(root, self)
        self.agregar_productos = self.crear_pantalla_agregar_productos(root)
        self.agregar_series = PantallaAgregarSeries(root, self.agregar_productos, self)
        self.resumen = PantallaResumen(root, self)

    def mostrar_bienvenida(self):
        self.bienvenida.mostrar()

    def mostrar_opciones(self):
        self.opciones.mostrar()

    def mostrar_formulario(self):
        self.formulario.mostrar()

    def mostrar_agregar_productos(self):
        self.agregar_productos.mostrar()

    def mostrar_agregar_series(self):
        self.agregar_series.mostrar()

    def mostrar_resumen(self):
        self.resumen.mostrar()

    def crear_pantalla_agregar_productos(self, root):
        # Obtener datos necesarios para PantallaAgregarProductos
        numero_guia = obtener_numero_guia()  # Reemplaza obtener_numero_guia con la lógica real
        nombre_empresa = obtener_nombre_empresa()  # Reemplaza obtener_nombre_empresa con la lógica real
        fecha = obtener_fecha()  # Reemplaza obtener_fecha con la lógica real
        cantidad_productos = obtener_cantidad_productos()  # Reemplaza obtener_cantidad_productos con la lógica real
        file_name1 = obtener_file_name1()  # Reemplaza obtener_file_name1 con la lógica real
        file_name2 = obtener_file_name2()  # Reemplaza obtener_file_name2 con la lógica real

        # Asegurarse de que cantidad_productos sea un valor válido
        cantidad_productos = cantidad_productos if cantidad_productos is not None else 0

        return PantallaAgregarProductos(root, numero_guia, nombre_empresa, fecha, cantidad_productos, file_name1, file_name2, self)

# Coloca las funciones de obtención de datos reales en lugar de obtener_numero_guia, obtener_nombre_empresa, etc.
def obtener_numero_guia():
    # Lógica para obtener el número de guía
    pass

def obtener_nombre_empresa():
    # Lógica para obtener el nombre de la empresa
    pass

def obtener_fecha():
    # Lógica para obtener la fecha
    pass

def obtener_cantidad_productos():
    # Lógica para obtener la cantidad de productos
    pass

def obtener_file_name1():
    # Lógica para obtener el nombre del archivo 1
    pass

def obtener_file_name2():
    # Lógica para obtener el nombre del archivo 2
    pass
