from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFileDialog, QDateEdit, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDate
import os
from app.data.data_manager import DataManager

class IngresarNuevoView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingresando nueva guía")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))  # Establecer el ícono de la ventana
        self.initUI()

    def initUI(self):
        # Tamaño de la pantalla completa
        screen_geometry = QDesktopWidget().availableGeometry()
        self.setGeometry(screen_geometry)

        # Título
        title_label = QLabel("Ingresando nueva guía")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 32px;")  # Tamaño de fuente 32

        # Número de Guía
        numero_guia_label = QLabel("Número de Guía:")
        numero_guia_label.setFixedWidth(120)  # Ancho del QLabel de 120 píxeles
        numero_guia_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.numero_guia_entry = QLineEdit()
        self.numero_guia_entry.setFixedWidth(150)  # Ancho del QLineEdit de 150 píxeles

        # Nombre de Empresa
        nombre_empresa_label = QLabel("Nombre de Empresa:")
        nombre_empresa_label.setFixedWidth(120)  # Ancho del QLabel de 120 píxeles
        nombre_empresa_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.nombre_empresa_entry = QLineEdit()
        self.nombre_empresa_entry.setFixedWidth(150)  # Ancho del QLineEdit de 150 píxeles

        # Fecha
        fecha_label = QLabel("Fecha:")
        fecha_label.setFixedWidth(120)  # Ancho del QLabel de 120 píxeles
        fecha_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.fecha_picker = QDateEdit()
        self.fecha_picker.setDate(QDate.currentDate())  # Fecha por default: fecha de hoy
        self.fecha_picker.setDisplayFormat("dd/MM/yyyy")
        self.fecha_picker.setFixedWidth(150)  # Ancho del QDateEdit de 150 píxeles

        # Cantidad de Productos
        cantidad_productos_label = QLabel("Cantidad de Productos:")
        cantidad_productos_label.setFixedWidth(120)  # Ancho del QLabel de 120 píxeles
        cantidad_productos_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.cantidad_productos_entry = QLineEdit()
        self.cantidad_productos_entry.setFixedWidth(150)  # Ancho del QLineEdit de 150 píxeles

        # Factura
        factura_label = QLabel("Archivo Factura:")
        factura_label.setFixedWidth(120)  # Ancho del QLabel de 120 píxeles
        factura_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.factura_file_label = QLabel("")  # Label para mostrar el nombre del archivo seleccionado
        self.factura_file_label.setWordWrap(True)  # Habilitar el ajuste de texto
        self.factura_file_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.factura_filename = ""  # Variable para guardar el nombre del PDF
        subir_factura_button = QPushButton("Subir archivo")
        subir_factura_button.setFixedWidth(80)  # Ancho del botón de subir archivo
        subir_factura_button.clicked.connect(self.upload_factura)

        # Guía
        guia_label = QLabel("Archivo Guía:")
        guia_label.setFixedWidth(120)  # Ancho del QLabel de 120 píxeles
        guia_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.guia_file_label = QLabel("")  # Label para mostrar el nombre del archivo seleccionado
        self.guia_file_label.setWordWrap(True)  # Habilitar el ajuste de texto
        self.guia_file_label.setAlignment(Qt.AlignLeft)  # Justificado a la izquierda
        self.guia_filename = ""  # Variable para guardar el nombre del PDF
        subir_guia_button = QPushButton("Subir archivo")
        subir_guia_button.setFixedWidth(80)  # Ancho del botón de subir archivo
        subir_guia_button.clicked.connect(self.upload_guia)

        # Botones de aceptar y cancelar
        aceptar_button = QPushButton("Continuar")
        aceptar_button.clicked.connect(self.continuar_ingreso)
        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cancelar)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(title_label)

        # Layout para los primeros 3 elementos
        first_row_layout = QHBoxLayout()
        first_row_layout.addWidget(numero_guia_label)
        first_row_layout.addWidget(self.numero_guia_entry)
        first_row_layout.addWidget(nombre_empresa_label)
        first_row_layout.addWidget(self.nombre_empresa_entry)
        first_row_layout.addWidget(fecha_label)
        first_row_layout.addWidget(self.fecha_picker)
        layout.addLayout(first_row_layout)

        # Layout para los siguientes 3 elementos
        second_row_layout = QHBoxLayout()
        second_row_layout.addWidget(cantidad_productos_label)
        second_row_layout.addWidget(self.cantidad_productos_entry)
        layout.addLayout(second_row_layout)

        # Layout para los archivos de factura y guía
        file_labels_layout = QHBoxLayout()
        file_labels_layout.addWidget(factura_label)
        file_labels_layout.addWidget(self.factura_file_label)
        file_labels_layout.addWidget(subir_factura_button)
        file_labels_layout.addWidget(guia_label)
        file_labels_layout.addWidget(self.guia_file_label)
        file_labels_layout.addWidget(subir_guia_button)
        layout.addLayout(file_labels_layout)

        # Layout para los botones de aceptar y cancelar
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(cancelar_button)  # Botón cancelar a la izquierda
        buttons_layout.addWidget(aceptar_button)  # Botón aceptar a la derecha
        buttons_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def validar_ingreso(self):
        # Validar que todos los campos estén llenos
        if (not self.numero_guia_entry.text().strip() or
            not self.nombre_empresa_entry.text().strip() or
            not self.fecha_picker.date().isValid() or
            not self.cantidad_productos_entry.text().strip() or
            not self.factura_file_label.text().strip() or
            not self.guia_file_label.text().strip()):
            QMessageBox.warning(self, "Error", "Llene todos los campos")
            return

        # Validar la fecha
        if self.fecha_picker.date().toPyDate() < QDate(2022, 1, 1).toPyDate():
            QMessageBox.warning(self, "Error", "Fecha ingresada incorrecta")
            return

        # Validar la cantidad de productos
        cantidad_productos = self.cantidad_productos_entry.text()
        if not cantidad_productos.isdigit() or not (1 <= int(cantidad_productos) <= 99):
            QMessageBox.warning(self, "Error", "Ingrese un número correcto en la cantidad de productos")
            return

        # Validar si se han subido guía y factura
        if self.factura_file_label.text() == self.guia_file_label.text():
            QMessageBox.warning(self, "Error", "Guía y factura deben ser diferentes")
            return

        return True

    def continuar_ingreso(self):
        # Validar ingreso antes de continuar
        if not self.validar_ingreso():
            return

        # Guardar datos en el DataManager
        data_manager = DataManager.get_instance()
        data_manager.guardar_datos_ingreso_nuevo(
            numero_guia=self.numero_guia_entry.text(),
            nombre_empresa=self.nombre_empresa_entry.text(),
            fecha=self.fecha_picker.date().toString("dd/MM/yyyy"),
            cantidad_productos=self.cantidad_productos_entry.text(),
            file_name_guia=self.guia_filename,
            file_name_factura=self.factura_filename,
            file_path_guia=self.guia_file_label.text(),
            file_path_factura=self.factura_file_label.text()
        )

        # Imprimir los datos por consola
        print("Número de Guía:", self.numero_guia_entry.text())
        print("Nombre de Empresa:", self.nombre_empresa_entry.text())
        print("Fecha:", self.fecha_picker.date().toString("dd/MM/yyyy"))
        print("Cantidad de Productos:", self.cantidad_productos_entry.text())
        print("Archivo Factura:", self.factura_filename)  # Imprimir solo el nombre del PDF
        print("Archivo Guía:", self.guia_filename)  # Imprimir solo el nombre del PDF

        # Cerrar esta ventana y abrir la siguiente
        self.close()
        self.controller.mostrar_ingreso_producto()

    def upload_factura(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar Factura", "", "Archivos PDF (*.pdf)")
        if filename:
            self.factura_file_label.setText(os.path.basename(filename))  # Mostrar solo el nombre del archivo
            self.factura_filename = os.path.basename(filename)  # Guardar el nombre del PDF

    def upload_guia(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar Guía", "", "Archivos PDF (*.pdf)")
        if filename:
            self.guia_file_label.setText(os.path.basename(filename))  # Mostrar solo el nombre del archivo
            self.guia_filename = os.path.basename(filename)  # Guardar el nombre del PDF

    def set_controller(self, controller):
        self.controller = controller

    def cancelar(self):
        self.close()
        self.controller.mostrar_opciones()
