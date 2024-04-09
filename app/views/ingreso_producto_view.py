from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
from app.data.data_manager import DataManager

class IngresoProductoView(QDialog):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Ingreso de Producto")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.initUI()

    def set_controller(self, controller):
        self.controller = controller

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel("Ingresa los datos de los productos")
        title_label.setStyleSheet("font-size: 15pt; font-weight: bold;")
        layout.addWidget(title_label)

        cantidad_productos = DataManager.get_instance().obtener_cantidad_productos()

        # Convertir la cantidad de productos a un entero
        cantidad_productos = int(cantidad_productos)

        for i in range(cantidad_productos):
            producto_layout = QVBoxLayout()
            producto_widget = QWidget()
            producto_widget.setLayout(producto_layout)

            producto_label = QLabel(f"Producto {i+1}:")
            producto_layout.addWidget(producto_label)

            nombre_label = QLabel("Nombre del producto:")
            nombre_entry = QLineEdit()
            producto_layout.addWidget(nombre_label)
            producto_layout.addWidget(nombre_entry)

            serie_label = QLabel("Series del producto:")
            serie_entry = QLineEdit()
            producto_layout.addWidget(serie_label)
            producto_layout.addWidget(serie_entry)

            # Botones de agregar y reestablecer serie
            botones_layout = QHBoxLayout()
            producto_layout.addLayout(botones_layout)

            agregar_button = QPushButton("Agregar")
            agregar_button.clicked.connect(lambda state, entry=serie_entry: self.agregar_serie(entry))
            botones_layout.addWidget(agregar_button)

            reestablecer_button = QPushButton("Reestablecer")
            reestablecer_button.clicked.connect(lambda state, entry=serie_entry: self.reestablecer_serie(entry))
            botones_layout.addWidget(reestablecer_button)

            layout.addWidget(producto_widget)

        botones_layout = QHBoxLayout()
        layout.addLayout(botones_layout)

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cancelar)
        botones_layout.addWidget(cancelar_button)

        continuar_button = QPushButton("Continuar")
        continuar_button.clicked.connect(self.mostrar_resumen_view)
        botones_layout.addWidget(continuar_button)

    def cancelar(self):
        self.close()

    def agregar_serie(self, entry):
        serie = entry.text()
        # Lógica para agregar la serie
        print(f"Agregar serie: {serie}")
        # Llamar al método en el controlador para mostrar la vista de agregar serie
        self.controller.mostrar_agregar_serie()

    def reestablecer_serie(self, entry):
        entry.setText("")  # Limpiar el texto del entry
        # Lógica para reestablecer la serie
        print("Serie reestablecida")

    def mostrar_resumen_view(self):
        print("Pasando los datos al resumen...")
