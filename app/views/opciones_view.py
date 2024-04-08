from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

class OpcionesView(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Opciones de la Aplicación")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))

        # Obtener tamaño de pantalla
        screen_geometry = QApplication.desktop().screenGeometry()
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())

        self.label = QLabel("¡Bienvenido a las opciones!", self)
        self.label.setFont(QFont("Arial", 15, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(20)

        self.buscar_producto_button = QPushButton(self)
        self.buscar_producto_button.setIcon(QIcon("resources/Busqueda.png"))
        self.buscar_producto_button.setIconSize(QSize(100, 100))
        self.buscar_producto_button.setText("BUSCAR PRODUCTO")
        self.buscar_producto_button.clicked.connect(self.buscar_producto)
        self.buscar_producto_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

        self.ingresar_nuevo_button = QPushButton(self)
        self.ingresar_nuevo_button.setIcon(QIcon("resources/IngresoGuia.png"))
        self.ingresar_nuevo_button.setIconSize(QSize(100, 100))
        self.ingresar_nuevo_button.setText("INGRESAR NUEVO")
        self.ingresar_nuevo_button.clicked.connect(self.ingresar_nuevo)
        self.ingresar_nuevo_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

        self.cerrar_button = QPushButton("Cerrar", self)
        self.cerrar_button.clicked.connect(self.cerrar_ventana)
        self.cerrar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.buscar_producto_button)
        buttons_layout.addWidget(self.ingresar_nuevo_button)
        layout.addLayout(buttons_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.cerrar_button)
        layout.addLayout(bottom_layout)

        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

    def set_controller(self, controller):
        self.controller = controller

    def buscar_producto(self):
        print("Buscar productos")
        # self.controller.mostrar_buscar_producto()

    def ingresar_nuevo(self):
        print("Ingresar productos")
        self.controller.mostrar_ingresar_nuevo()

    def cerrar_ventana(self):
        self.close()
        self.controller.show_bienvenida()
