import os

class DatosModel:
    def __init__(self):
        self.numero_guia = None
        self.nombre_empresa = None
        self.fecha = None
        self.cantidad_productos = None
        self.file_name_guia = None
        self.file_name_factura = None
        self.ruta_base = os.path.join(os.path.dirname(__file__), "..", "Documents")

        os.makedirs(os.path.join(self.ruta_base, "Guias"), exist_ok=True)
        os.makedirs(os.path.join(self.ruta_base, "Facturas"), exist_ok=True)

    def set_datos(self, numero_guia, nombre_empresa, fecha, cantidad_productos, file_name_guia, file_name_factura):
        self.numero_guia = numero_guia
        self.nombre_empresa = nombre_empresa
        self.fecha = fecha
        self.cantidad_productos = cantidad_productos
        self.file_name_guia = file_name_guia
        self.file_name_factura = file_name_factura

    def get_ruta_guia(self):
        return os.path.join(self.ruta_base, "Guias", self.file_name_guia)

    def get_ruta_factura(self):
        return os.path.join(self.ruta_base, "Facturas", self.file_name_factura)
