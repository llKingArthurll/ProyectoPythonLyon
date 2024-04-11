from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class AgregarSerieView(QDialog):
    def __init__(self, entry_target, parent_view):
        super().__init__()
        self.entry_target = entry_target
        self.parent_view = parent_view
        self.setWindowTitle("Agregar Serie")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Agregar Serie:")
        layout.addWidget(label)

        self.entry_serie = QLineEdit()
        layout.addWidget(self.entry_serie)
        self.entry_serie.setFocus()

        button_container = QHBoxLayout()
        layout.addLayout(button_container)

        button_agregar = QPushButton("Agregar")
        button_agregar.clicked.connect(self.agregar_serie)
        button_container.addWidget(button_agregar)

        button_listo = QPushButton("Listo")
        button_listo.clicked.connect(self.cerrar_ventana)
        button_container.addWidget(button_listo)

        # Vincular el evento de presionar Enter al método agregar_serie
        self.entry_serie.returnPressed.connect(self.agregar_serie)

    def agregar_serie(self):
        serie = self.entry_serie.text()

        if serie:
            entry_target_value = self.entry_target.text()
            nueva_serie = f"{entry_target_value}, {serie}" if entry_target_value else serie
            self.entry_target.setText(nueva_serie)
            self.entry_serie.clear()
            self.entry_serie.setFocus()

    def cerrar_ventana(self):
        self.accept()
