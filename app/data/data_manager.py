class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.data = {}
            # Inicializar una lista para almacenar los productos con sus series
            self.productos_con_series = []

    def guardar_datos_ingreso_nuevo(self, numero_guia, nombre_empresa, fecha, cantidad_productos, ruta_guia, ruta_factura):
        self.data['numero_guia'] = numero_guia
        self.data['nombre_empresa'] = nombre_empresa
        self.data['fecha'] = fecha
        self.data['cantidad_productos'] = cantidad_productos
        self.data['ruta_guia'] = ruta_guia
        self.data['ruta_factura'] = ruta_factura

    def obtener_numero_guia(self):
        return self.data.get('numero_guia')

    def obtener_nombre_empresa(self):
        return self.data.get('nombre_empresa')

    def obtener_fecha(self):
        return self.data.get('fecha')

    def obtener_cantidad_productos(self):
        return self.data.get('cantidad_productos')

    def obtener_ruta_guia(self):
        return self.data.get('ruta_guia')

    def obtener_ruta_factura(self):
        return self.data.get('ruta_factura')

    def guardar_datos_productos(self, datos_productos):
        """
        Guarda los datos de los productos con sus series.
        datos_productos debe ser una lista de diccionarios donde cada diccionario representa un producto
        con su nombre y una lista de sus series.
        """
        self.productos_con_series = datos_productos

    def obtener_productos_con_series(self):
        """
        Devuelve la lista de diccionarios con los productos y sus series.
        """
        return self.productos_con_series

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
