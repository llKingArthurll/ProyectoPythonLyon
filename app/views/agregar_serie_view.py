<<<<<<< HEAD
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
=======
import tkinter as tk
import keyboard
from PIL import Image, ImageTk

>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

class AgregarSerieView(QDialog):
    def __init__(self, entry_target, parent_view):
        super().__init__()
        self.entry_target = entry_target
<<<<<<< HEAD
        self.parent_view = parent_view
        self.setWindowTitle("Agregar Serie")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.initUI()
=======
        self.pantalla_agregar_productos = pantalla_agregar_productos
        self.root.title("Agregar Serie")
        self.root.resizable(width=False, height=False)
        self.root.geometry("300x130")
        self.root.iconbitmap("resources/LogoLyon.ico")
        
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Agregar Serie:")
        layout.addWidget(label)

<<<<<<< HEAD
        self.entry_serie = QLineEdit()
        layout.addWidget(self.entry_serie)
        self.entry_serie.setFocus()
=======
        button_listo = tk.Button(self.root, text="Listo", command=self.cerrar_ventana, width=10,  bg="#FE6E0C",fg="white")
        button_listo.pack(side="bottom", pady=10)
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

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
