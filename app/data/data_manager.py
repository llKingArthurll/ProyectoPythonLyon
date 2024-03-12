import os
import shutil
from datetime import datetime

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
            self.numero_guia = None
            self.nombre_empresa = None
            self.fecha = None
            self.cantidad_productos = None
            self.file_name_guia = None
            self.file_name_factura = None
            self.file_path_guia = None
            self.file_path_factura = None
            self.ingreso_producto_data = None

    def set_data(self, numero_guia, nombre_empresa, fecha, cantidad_productos, file_name_guia, file_name_factura, file_path_guia, file_path_factura):
        self.numero_guia = numero_guia
        self.nombre_empresa = nombre_empresa
        self.fecha = fecha
        self.cantidad_productos = cantidad_productos
        self.file_name_guia = file_name_guia
        self.file_name_factura = file_name_factura
        self.file_path_guia = file_path_guia
        self.file_path_factura = file_path_factura

    def set_ingreso_producto_data(self, ingreso_producto_data):
        self.ingreso_producto_data = ingreso_producto_data

    def get_numero_guia(self):
        return self.numero_guia

    def get_nombre_empresa(self):
        return self.nombre_empresa

    def get_fecha(self):
        return self.fecha

    def get_cantidad_productos(self):
        return self.cantidad_productos

    def get_file_name_guia(self):
        return self.file_name_guia

    def get_file_name_factura(self):
        return self.file_name_factura
    
    def get_file_path_guia(self):
        return self.file_path_guia
    
    def get_file_path_factura(self):
        return self.file_path_factura

    def get_ingreso_producto_data(self):
        return self.ingreso_producto_data

    def get_ingreso_producto_data(self):
        return self.ingreso_producto_data

    def get_fecha_actual(self):
        now = datetime.now()
        fecha_actual = now.strftime("%d-%m-%Y %H:%M:%S")
        return fecha_actual

    def clear_data(self):
        self.numero_guia = None
        self.nombre_empresa = None
        self.fecha = None
        self.cantidad_productos = None
        self.file_name_guia = None
        self.file_name_factura = None
        self.ingreso_producto_data = None

    def save_files(self):
        main_folder_path_guia = None
        main_folder_path_factura = None
        script_directory = os.path.dirname(os.path.abspath(__file__))
        documents_directory = os.path.join(script_directory, '..', '..', 'documents')
        if self.file_name_guia:
            main_folder_path_guia = self._move_file(documents_directory, self.file_name_guia, self.file_path_guia, subfolder="guia")
        if self.file_name_factura:
            main_folder_path_factura = self._move_file(documents_directory, self.file_name_factura, self.file_path_factura, subfolder="factura")
        return main_folder_path_guia, main_folder_path_factura

    def _move_file(self, directory, file_name, file_path, subfolder=None):
        main_folder = directory
        if subfolder:
            subfolder_path = os.path.join(main_folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            destination_path = os.path.join(subfolder_path, file_name)
        else:
            destination_path = os.path.join(main_folder, file_name)

        print(f"Moviendo archivo desde {file_path} a {destination_path}")
        try:
            shutil.move(file_path, destination_path)
        except FileNotFoundError:
            print(f"Error: Archivo {file_name} no encontrado en el directorio temporal.")
        return destination_path
    
    def _rename_file(self, file_path, new_file_name):
        directory, old_file_name = os.path.split(file_path)
        new_file_path = os.path.join(directory, new_file_name)
        
        print(f"Cambiando el nombre de {old_file_name} a {new_file_name}")
        try:
            os.rename(file_path, new_file_path)
        except FileNotFoundError:
            print(f"Error: Archivo {old_file_name} no encontrado en el directorio temporal.")
        
        return new_file_path

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
