from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QApplication, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

class BienvenidaView(QDialog):
    def __init__(self):
        super().__init__()

        # Obtener la resolución de la pantalla
        screen_resolution = QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()

        self.setWindowTitle("LYON SYSTEM")
        self.setGeometry(0, 0, width, height)
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))

        self.title_label = QLabel("Bienvenido(a) al Sistema", self)
        self.title_label.setFont(QFont("Verdana", 25))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: black;")
        self.title_label.setMargin(10)

        imagen_path = "resources/logoFondo.png"
        self.imagen_label = QLabel(self)
        pixmap = QPixmap(imagen_path)
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignCenter)
        self.imagen_label.setMargin(10)

        self.continuar_button = QPushButton("Continuar", self)
        self.continuar_button.setFixedWidth(200)
        self.continuar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)
        self.continuar_button.clicked.connect(self.continuar)

        # Crear un layout horizontal para el botón
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.continuar_button)
        button_layout.setAlignment(Qt.AlignCenter)

        # Crear un layout vertical para todos los widgets
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.imagen_label)
        main_layout.addLayout(button_layout)
        main_layout.setAlignment(Qt.AlignCenter)

        self.setLayout(main_layout)

    def continuar(self):
        print("Se cambió de pantalla a Opciones")
        self.close()
        self.controller.mostrar_opciones()

    def set_controller(self, controller):
        self.controller = controller
