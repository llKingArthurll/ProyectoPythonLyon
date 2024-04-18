from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFileDialog, QDateEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDate
import os
from app.data.data_manager import DataManager

class IngresarNuevoView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingresando nueva guía")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.showMaximized()
        
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Primer layout horizontal (solo título)
        title_layout = QHBoxLayout()
        title_label = QLabel("Ingresando nueva guía")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 32px;")
        title_layout.addWidget(title_label)
        main_layout.addLayout(title_layout)

        # Segundo layout horizontal (Número de guía, Nombre de empresa, Fecha)
        guia_empresa_fecha_layout = QHBoxLayout()
        # Número de Guía
        numero_guia_label = QLabel("Número de Guía:")
        numero_guia_label.setFixedWidth(120)
        self.numero_guia_entry = QLineEdit()
        self.numero_guia_entry.setFixedWidth(200)
        self.numero_guia_entry.setPlaceholderText("Número de guía aquí...")
        # Nombre de Empresa
        nombre_empresa_label = QLabel("Nombre de Empresa:")
        nombre_empresa_label.setFixedWidth(120)
        self.nombre_empresa_entry = QLineEdit()
        self.nombre_empresa_entry.setFixedWidth(200)
        self.nombre_empresa_entry.setPlaceholderText("Nombre de empresa aquí...")
        # Fecha
        fecha_label = QLabel("Fecha:")
        fecha_label.setFixedWidth(120)
        self.fecha_picker = QDateEdit()
        self.fecha_picker.setFixedWidth(120)
        self.fecha_picker.setDate(QDate.currentDate())
        self.fecha_picker.setDisplayFormat("dd/MM/yyyy")

        # Añadir elementos al layout
        guia_empresa_fecha_layout.addWidget(numero_guia_label)
        guia_empresa_fecha_layout.addWidget(self.numero_guia_entry)
        guia_empresa_fecha_layout.addWidget(nombre_empresa_label)
        guia_empresa_fecha_layout.addWidget(self.nombre_empresa_entry)
        guia_empresa_fecha_layout.addWidget(fecha_label)
        guia_empresa_fecha_layout.addWidget(self.fecha_picker)
        main_layout.addLayout(guia_empresa_fecha_layout)

        # Tercer layout horizontal (Cantidad de productos, Archivo Factura, Archivo Guía)
        productos_factura_guia_layout = QHBoxLayout()
        # Cantidad de Productos
        cantidad_productos_label = QLabel("Cantidad de Productos:")
        cantidad_productos_label.setFixedWidth(120)
        self.cantidad_productos_entry = QLineEdit()
        self.cantidad_productos_entry.setFixedWidth(200)
        self.cantidad_productos_entry.setPlaceholderText("Números entre 1 y 99")
        # Archivo Factura
        factura_label = QLabel("Archivo Factura:")
        factura_label.setFixedWidth(120)
        self.factura_file_label = QLabel("")
        subir_factura_button = QPushButton("Subir archivo")
        subir_factura_button.setFixedWidth(150)
        subir_factura_button.clicked.connect(self.upload_factura)
        # Archivo Guía
        guia_label = QLabel("Archivo Guía:")
        guia_label.setFixedWidth(120)
        self.guia_file_label = QLabel("")
        subir_guia_button = QPushButton("Subir archivo")
        subir_guia_button.setFixedWidth(150)
        subir_guia_button.clicked.connect(self.upload_guia)

        # Añadir elementos al layout
        productos_factura_guia_layout.addWidget(cantidad_productos_label)
        productos_factura_guia_layout.addWidget(self.cantidad_productos_entry)
        productos_factura_guia_layout.addWidget(factura_label)
        productos_factura_guia_layout.addWidget(subir_factura_button)
        productos_factura_guia_layout.addWidget(guia_label)
        productos_factura_guia_layout.addWidget(subir_guia_button)
        main_layout.addLayout(productos_factura_guia_layout)

        # Cuarto layout horizontal (Labels para mostrar nombres de los archivos)
        file_labels_layout = QHBoxLayout()
        file_labels_layout.addWidget(self.factura_file_label)
        file_labels_layout.addWidget(self.guia_file_label)
        main_layout.addLayout(file_labels_layout)

        # Quinto layout horizontal (Botones de cancelar y continuar)
        buttons_layout = QHBoxLayout()
        cancelar_button = QPushButton("Cancelar")
        cancelar_button.setFixedWidth(150)
        cancelar_button.clicked.connect(self.cancelar)
        aceptar_button = QPushButton("Continuar")
        aceptar_button.setFixedWidth(150)
        aceptar_button.clicked.connect(self.continuar_ingreso)
        
        # Añadir botones al layout
        buttons_layout.addWidget(cancelar_button)
        buttons_layout.addWidget(aceptar_button)
        main_layout.addLayout(buttons_layout)

        # Asignar el layout principal a la ventana
        self.setLayout(main_layout)

    def validar_ingreso(self):
        # Limpiar espacios en blanco del texto ingresado en el campo de cantidad
        cantidad_texto = self.cantidad_productos_entry.text().strip()

        # Validar que todos los campos estén llenos
        if (not self.numero_guia_entry.text().strip() or
            not self.nombre_empresa_entry.text().strip() or
            not self.fecha_picker.date().isValid() or
            not cantidad_texto or
            not self.factura_file_label.text().strip() or
            not self.guia_file_label.text().strip()):
            QMessageBox.warning(self, "Error", "Llene todos los campos")
            return

        # Validar la fecha
        if self.fecha_picker.date().toPyDate() < QDate(2022, 1, 1).toPyDate():
            QMessageBox.warning(self, "Error", "Fecha ingresada incorrecta")
            return

        # Validar la cantidad de productos
        if not cantidad_texto.isdigit() or not (1 <= int(cantidad_texto) <= 99):
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
            cantidad_productos=self.cantidad_productos_entry.text().strip(),
            ruta_factura=self.factura_filename,
            ruta_guia=self.guia_filename
        )

        # Cerrar esta ventana y abrir la siguiente
        self.close()
        self.controller.mostrar_ingreso_producto()

    def upload_factura(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar Factura", "", "Archivos PDF (*.pdf)")
        if filename:
            self.factura_file_label.setText(os.path.basename(filename))
            self.factura_filename = filename

    def upload_guia(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar Guía", "", "Archivos PDF (*.pdf)")
        if filename:
            self.guia_file_label.setText(os.path.basename(filename))
            self.guia_filename = filename

    def set_controller(self, controller):
        self.controller = controller

    def cancelar(self):
        self.close()
        self.controller.mostrar_opciones()
