from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime
from PyQt5.QtCore import Qt
from app.data.data_manager import DataManager

class ResumenProductoView(QDialog):
    def __init__(self, controller=None):
        super().__init__()
        self.setWindowTitle("Resumen de Productos")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.setFixedSize(800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Título centrado para el resumen
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

        # Mostrar los datos en QLabel
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
            for producto in productos:
                nombre_producto = producto['nombre']
                series = producto['series']

                # Mostrar nombre del producto
                producto_label = QLabel(f"Producto: {nombre_producto}")
                layout.addWidget(producto_label)

                # Mostrar series asociadas al producto
                for serie in series:
                    serie_label = QLabel(f"Serie: {serie}")
                    layout.addWidget(serie_label)

        # Botones de continuar y cancelar
        botones_layout = QHBoxLayout()
        layout.addLayout(botones_layout)

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cancelar)
        botones_layout.addWidget(cancelar_button)

        continuar_button = QPushButton("Continuar")
        continuar_button.clicked.connect(self.continuar)
        botones_layout.addWidget(continuar_button)

    def mostrar_hora_actual(self):
        hora_actual = QTime.currentTime()
        hora_formateada = hora_actual.toString("hh:mm:ss:zzz")
        print(f"Hora actual: {hora_formateada}")
    
    def cancelar(self):
        self.close()
        if self.controller:
            self.controller.mostrar_ingresar_nuevo()

    def continuar(self):
        self.mostrar_hora_actual()
        # if self.controller:
        #     self.controller.continuar_proceso()

    def set_controller(self, controller):
        self.controller = controller
