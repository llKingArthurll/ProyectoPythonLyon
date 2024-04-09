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

    def guardar_datos_ingreso_nuevo(self, numero_guia, nombre_empresa, fecha, cantidad_productos, ruta_guia, ruta_factura):
        self.data['numero_guia'] = numero_guia
        self.data['nombre_empresa'] = nombre_empresa
        self.data['fecha'] = fecha
        self.data['cantidad_productos'] = cantidad_productos
        self.data['ruta_guia'] = ruta_guia
        self.data['ruta_factura'] = ruta_factura

    def obtener_datos_ingreso_nuevo(self):
        return (
            self.data.get('numero_guia'),
            self.data.get('nombre_empresa'),
            self.data.get('fecha'),
            self.data.get('cantidad_productos'),
            self.data.get('ruta_guia'),
            self.data.get('ruta_factura')
        )

    def obtener_cantidad_productos(self):
        return self.data.get('cantidad_productos')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# import os
# import shutil
# from datetime import datetime

# class DataManager:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(DataManager, cls).__new__(cls)
#             cls._instance._initialized = False
#         return cls._instance

#     def __init__(self):
#         if not self._initialized:
#             self._initialized = True
#             self.id_nuevoingreso = None
#             self.nombre_guia = None
#             self.nombre_empresa = None
#             self.cantidad_productos = None
#             self.fecha_guia = None
#             self.save_data = None
#             self.path_guia = None
#             self.path_factura = None
#             self.productos_data = None

#     def set_data(self, numero_guia, nombre_empresa, fecha, cantidad_productos, file_name_guia, file_name_factura, file_path_guia, file_path_factura):
#         self.numero_guia = numero_guia
#         self.nombre_empresa = nombre_empresa
#         self.fecha = fecha
#         self.cantidad_productos = cantidad_productos
#         self.file_name_guia = file_name_guia
#         self.file_name_factura = file_name_factura
#         self.file_path_guia = file_path_guia
#         self.file_path_factura = file_path_factura

#     def set_id_nuevoingreso(self, id_nuevoingreso):
#         self.id_nuevoingreso = id_nuevoingreso

#     def set_productos_data(self, productos_data):
#         self.productos_data = productos_data

#     def get_id_nuevoingreso(self):
#         return self.id_nuevoingreso

#     def get_numero_guia(self):
#         return self.numero_guia

#     def get_nombre_empresa(self):
#         return self.nombre_empresa

#     def get_cantidad_productos(self):
#         return self.cantidad_productos

#     def get_fecha(self):
#         return self.fecha_guia

#     def get_save_data(self):
#         return self.save_data

#     def get_path_guia(self):
#         return self.path_guia

#     def get_path_factura(self):
#         return self.path_factura

#     def get_ingreso_producto_data(self):
#         return self.productos_data

#     def get_fecha_actual(self):
#         now = datetime.now()
#         fecha_actual = now.strftime("%d-%m-%Y %H:%M:%S")
#         return fecha_actual

#     def clear_data(self):
#         self.id_nuevoingreso = None
#         self.nombre_guia = None
#         self.nombre_empresa = None
#         self.cantidad_productos = None
#         self.fecha_guia = None
#         self.save_data = None
#         self.path_guia = None
#         self.path_factura = None
#         self.productos_data = None

#     def save_files(self):
#         main_folder_path_guia = None
#         main_folder_path_factura = None
#         script_directory = os.path.dirname(os.path.abspath(__file__))
#         documents_directory = os.path.join(script_directory, '..', '..', 'documents')
#         if self.path_guia:
#             main_folder_path_guia = self._move_file(documents_directory, os.path.basename(self.path_guia), self.path_guia, subfolder="guia")
#         if self.path_factura:
#             main_folder_path_factura = self._move_file(documents_directory, os.path.basename(self.path_factura), self.path_factura, subfolder="factura")
#         return main_folder_path_guia, main_folder_path_factura

#     def _move_file(self, directory, file_name, file_path, subfolder=None):
#         main_folder = directory
#         if subfolder:
#             subfolder_path = os.path.join(main_folder, subfolder)
#             if not os.path.exists(subfolder_path):
#                 os.makedirs(subfolder_path)
#             destination_path = os.path.join(subfolder_path, file_name)
#         else:
#             destination_path = os.path.join(main_folder, file_name)

#         print(f"Moviendo archivo desde {file_path} a {destination_path}")
#         try:
#             shutil.move(file_path, destination_path)
#         except FileNotFoundError:
#             print(f"Error: Archivo {file_name} no encontrado en el directorio temporal.")
#         return destination_path
    
#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls()
#         return cls._instance
