import os
import shutil
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from app.data.data_manager import DataManager
from app.data.db_queries import DatabaseQueries

class ResumenProductoView(QWidget):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Resumen de Productos")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.setFixedSize(600, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        resumen_label = QLabel("Resumen de lo ingresado")
        resumen_label.setAlignment(Qt.AlignCenter)
        resumen_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        layout.addWidget(resumen_label)

        numero_guia = DataManager.get_instance().obtener_numero_guia()
        nombre_empresa = DataManager.get_instance().obtener_nombre_empresa()
        fecha = DataManager.get_instance().obtener_fecha()
        cantidad_productos = DataManager.get_instance().obtener_cantidad_productos()
        productos = DataManager.get_instance().obtener_productos_con_series()

        for label_text, value_text in [("Número de Guía", numero_guia),
                                       ("Nombre de Empresa", nombre_empresa),
                                       ("Fecha", fecha),
                                       ("Cantidad de Productos", cantidad_productos)]:
            label = QLabel(label_text + ":")
            line_edit = QLineEdit(value_text)
            line_edit.setEnabled(False)
            layout.addWidget(label)
            layout.addWidget(line_edit)

        if productos:
            table = QTableWidget()
            table.setColumnCount(2)
            table.setHorizontalHeaderLabels(["Nombre", "Series"])

            for producto in productos:
                nombre_producto = producto['nombre']
                series = ", ".join(producto['series'])
                row_position = table.rowCount()
                table.insertRow(row_position)
                item_nombre = QTableWidgetItem(nombre_producto)
                item_nombre.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, 0, item_nombre)
                item_series = QTableWidgetItem(series)
                item_series.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, 1, item_series)

            table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
            table.setEditTriggers(QTableWidget.NoEditTriggers)
            table.setSelectionMode(QTableWidget.NoSelection)

            header = table.horizontalHeader()
            header.setStyleSheet("background-color: #333333; color: black;")
            header.setSectionResizeMode(QHeaderView.Stretch)

            table.setStyleSheet("""
                QTableWidget {
                    border: 1px solid #CCCCCC;
                }
                QTableWidget::item {
                    padding: 5px;
                }
            """)
            
            layout.addWidget(table)

        botones_layout = QHBoxLayout()
        layout.addLayout(botones_layout)

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.setFixedWidth(150)
        cancelar_button.clicked.connect(self.cancelar)
        botones_layout.addWidget(cancelar_button)
        cancelar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
        """)   

        guardar_button = QPushButton("Guardar")
        guardar_button.setFixedWidth(150)
        guardar_button.clicked.connect(self.guardar)
        botones_layout.addWidget(guardar_button)
        guardar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
        """)   

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
        
        numero_guia = data_manager.obtener_numero_guia()
        nombre_empresa = data_manager.obtener_nombre_empresa()
        fecha = data_manager.obtener_fecha()
        cantidad_productos = data_manager.obtener_cantidad_productos()
        
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
        
        productos = data_manager.obtener_productos_con_series()
        
        try:
            DatabaseQueries.insertar_productos(id_nuevo_ingreso, productos)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al guardar los productos: {e}")

    def guardar(self):
        nueva_ruta_guia, nueva_ruta_factura = self.mover_archivos()
        
        if nueva_ruta_guia is None or nueva_ruta_factura is None:
            return
        
        id_nuevo_ingreso = self.guardar_datos_ingreso(nueva_ruta_guia, nueva_ruta_factura)
        
        if id_nuevo_ingreso is None:
            QMessageBox.warning(self, "Error", "Error al guardar los datos de ingreso en la base de datos.")
            return
        
        self.guardar_datos_productos(id_nuevo_ingreso)
        
        QMessageBox.information(
            self, 
            "Confirmación",
            "Se guardó satisfactoriamente en la base de datos.",
            QMessageBox.Ok
        )
        
        data_manager = DataManager.get_instance()
        data_manager.limpiar_datos()
        
        self.close()
        
        if self.controller:
            self.controller.mostrar_opciones()

    def set_controller(self, controller):
        self.controller = controller
