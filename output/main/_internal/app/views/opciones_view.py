from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from app.config.screen_config import configuracion_window, configuracion_tamano_pantalla

class OpcionesView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Opciones de la Aplicación")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))

        # Obtener tamaño de pantalla
        screen_geometry = QApplication.desktop().screenGeometry()
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())
        self.showMaximized()

        self.label = QLabel("¡Bienvenido a las opciones!", self)
        self.label.setFont(QFont("Arial", 15, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(20)

        self.buscar_producto_button = QPushButton(self)
        self.buscar_producto_button.setIcon(QIcon("resources/Busqueda.png"))
        self.buscar_producto_button.setIconSize(QSize(100, 100))
        self.buscar_producto_button.setText("BUSCAR PRODUCTO")
        self.buscar_producto_button.setFixedSize(300, 200)
        self.buscar_producto_button.clicked.connect(self.buscar_producto)
        self.buscar_producto_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin-left: 20px;
                margin-right: 20px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

        self.ingresar_nuevo_button = QPushButton(self)
        self.ingresar_nuevo_button.setIcon(QIcon("resources/IngresoGuia.png"))
        self.ingresar_nuevo_button.setIconSize(QSize(100, 100))
        self.ingresar_nuevo_button.setText("INGRESAR NUEVO")
        self.ingresar_nuevo_button.setFixedSize(300, 200)
        self.ingresar_nuevo_button.clicked.connect(self.ingresar_nuevo)
        self.ingresar_nuevo_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin-left: 20px;
                margin-right: 20px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

        self.cerrar_button = QPushButton("Salir", self)
        self.cerrar_button.setFixedWidth(150)
        self.cerrar_button.clicked.connect(self.salir)
        self.cerrar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin-top: 50px;
                margin-left: 20px;
                margin-right: 20px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # Layout vertical para el botón de buscar producto
        buscar_layout = QVBoxLayout()
        buscar_layout.addWidget(self.buscar_producto_button)
        buscar_layout.setAlignment(Qt.AlignCenter)

        # Layout vertical para el botón de ingresar nuevo
        ingresar_layout = QVBoxLayout()
        ingresar_layout.addWidget(self.ingresar_nuevo_button)
        ingresar_layout.setAlignment(Qt.AlignCenter)

        buttons_layout = QHBoxLayout()
        buttons_layout.addLayout(buscar_layout)
        buttons_layout.addLayout(ingresar_layout)
        layout.addLayout(buttons_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.cerrar_button)
        layout.addLayout(bottom_layout)

        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

    def set_controller(self, controller):
        self.controller = controller

    def buscar_producto(self):
        self.close()
        self.controller.mostrar_buscar_producto()

    def ingresar_nuevo(self):
        self.controller.mostrar_ingresar_nuevo()

    def salir(self):
        self.close()
