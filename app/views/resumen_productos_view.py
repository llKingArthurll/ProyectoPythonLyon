import os
import shutil
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from app.data.data_manager import DataManager
from app.data.db_queries import DatabaseQueries

class ResumenProductoView(QDialog):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Resumen de Productos")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.setFixedSize(800, 600)
        self.initUI()

    def initUI(self):
        # Crear un layout vertical para justificar el contenido hacia la parte superior
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        # Título para el resumen
        resumen_label = QLabel("Resumen de lo ingresado")
        resumen_label.setAlignment(Qt.AlignCenter)
        resumen_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        layout.addWidget(resumen_label)

        # Obtener los datos del DataManager
        numero_guia = DataManager.get_instance().obtener_numero_guia()
        nombre_empresa = DataManager.get_instance().obtener_nombre_empresa()
        fecha = DataManager.get_instance().obtener_fecha()
        cantidad_productos = DataManager.get_instance().obtener_cantidad_productos()
        productos = DataManager.get_instance().obtener_productos_con_series()

        # Mostrar los datos generales
        numero_guia_label = QLabel(f"Número de Guía: {numero_guia}")
        layout.addWidget(numero_guia_label)

        nombre_empresa_label = QLabel(f"Nombre de Empresa: {nombre_empresa}")
        layout.addWidget(nombre_empresa_label)

        fecha_label = QLabel(f"Fecha: {fecha}")
        layout.addWidget(fecha_label)

        cantidad_productos_label = QLabel(f"Cantidad de Productos: {cantidad_productos}")
        layout.addWidget(cantidad_productos_label)

        # Mostrar los productos ingresados con sus series
        if productos:
            for idx, producto in enumerate(productos):
                nombre_producto = producto['nombre']
                series = producto['series']

                # Mostrar Producto con su número
                producto_label = QLabel(f"Producto {idx + 1}:")
                layout.addWidget(producto_label)

                # Mostrar nombre del producto
                nombre_label = QLabel(f"Nombre: {nombre_producto}")
                layout.addWidget(nombre_label)

                # Mostrar las series del producto
                series_label = QLabel(f"Series: {', '.join(series)}")
                layout.addWidget(series_label)

        # Botones de continuar y cancelar
        botones_layout = QHBoxLayout()
        layout.addLayout(botones_layout)

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.setFixedWidth(150)
        cancelar_button.clicked.connect(self.cancelar)
        botones_layout.addWidget(cancelar_button)

        continuar_button = QPushButton("Continuar")
        continuar_button.setFixedWidth(150)
        continuar_button.clicked.connect(self.continuar)
        botones_layout.addWidget(continuar_button)

    def cancelar(self):
        self.close()
        if self.controller:
            self.controller.mostrar_ingresar_nuevo()

    def mover_archivos(self):
        data_manager = DataManager.get_instance()
        
        ruta_guia = data_manager.obtener_ruta_guia()
        ruta_factura = data_manager.obtener_ruta_factura()
        
        nueva_ruta_guia = os.path.join("documents", "factura", os.path.basename(ruta_guia))
        nueva_ruta_factura = os.path.join("documents", "guia", os.path.basename(ruta_factura))
        
        try:
            shutil.move(ruta_guia, nueva_ruta_guia)
            print(f"Archivo de guía movido a: {nueva_ruta_guia}")
            
            shutil.move(ruta_factura, nueva_ruta_factura)
            print(f"Archivo de factura movido a: {nueva_ruta_factura}")
            
            return nueva_ruta_guia, nueva_ruta_factura
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al mover los archivos: {e}")
            return None, None

    def guardar_datos_ingreso(self, nueva_ruta_guia, nueva_ruta_factura):
        data_manager = DataManager.get_instance()
        
        # Obtener los datos de ingreso
        numero_guia = data_manager.obtener_numero_guia()
        nombre_empresa = data_manager.obtener_nombre_empresa()
        fecha = data_manager.obtener_fecha()
        cantidad_productos = data_manager.obtener_cantidad_productos()
        
        # Guardar los datos en la base de datos
        return DatabaseQueries.insertar_nuevo_ingreso(
            numero_guia=numero_guia,
            nombre_empresa=nombre_empresa,
            cantidad_productos=cantidad_productos,
            fecha=fecha,
            ruta_guia=nueva_ruta_guia,
            ruta_factura=nueva_ruta_factura
        )

    def guardar_datos_productos(self, id_nuevo_ingreso):
        data_manager = DataManager.get_instance()
        
        # Obtener los productos con sus series
        productos = data_manager.obtener_productos_con_series()
        
        try:
            # Guardar los productos en la base de datos
            DatabaseQueries.insertar_productos(id_nuevo_ingreso, productos)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al guardar los productos: {e}")

    def continuar(self):
        nueva_ruta_guia, nueva_ruta_factura = self.mover_archivos()
        
        if nueva_ruta_guia is None or nueva_ruta_factura is None:
            return
        
        id_nuevo_ingreso = self.guardar_datos_ingreso(nueva_ruta_guia, nueva_ruta_factura)
        
        if id_nuevo_ingreso is None:
            QMessageBox.warning(self, "Error", "Error al guardar los datos de ingreso en la base de datos.")
            return
        
        self.guardar_datos_productos(id_nuevo_ingreso)
        
        confirmacion = QMessageBox.information(
            self, 
            "Confirmación",
            "Se guardó satisfactoriamente en la base de datos.",
            QMessageBox.Ok
        )
        
        self.close()
        
        if self.controller:
            self.controller.mostrar_opciones()

    def set_controller(self, controller):
        self.controller = controller
