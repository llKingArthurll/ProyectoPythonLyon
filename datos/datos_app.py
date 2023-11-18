# datos/datos_app.py

class DatosApp:
    numero_guia = None
    nombre_empresa = None
    fecha = None
    cantidad_productos = None
    file_name_guia = None
    file_name_factura = None
    file_content_guia = None
    file_content_factura = None
    productos_guardados = None

    @classmethod
    def reset(cls):
        # Método para restablecer las variables a sus valores iniciales
        cls.numero_guia = None
        cls.nombre_empresa = None
        cls.fecha = None
        cls.cantidad_productos = None
        cls.file_name_guia = None
        cls.file_name_factura = None
        cls.file_content_guia = None
        cls.file_content_factura = None
        cls.productos_guardados = None
