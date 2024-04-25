from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout,
    QFileDialog, QDateEdit, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDate
import os
from app.data.data_manager import DataManager

class IngresarNuevoView(QWidget):
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager.get_instance()
        self.setWindowTitle("Ingresando nueva guía")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.showMaximized()
        self.initUI()
        self.cargar_datos()

    def initUI(self):
        # Layout principal centrado horizontalmente
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter)

        # Layout para el título justificado hacia arriba
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_label = QLabel("Ingresando nueva guía")
        title_label.setStyleSheet("font-size: 32px;")
        title_layout.addWidget(title_label)

        # Layout que contiene los layouts secundarios
        main_content_layout = QVBoxLayout()
        main_content_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Layout para número de guía, nombre de empresa y fecha
        guia_empresa_fecha_layout = QHBoxLayout()
        guia_empresa_fecha_layout.setAlignment(Qt.AlignHCenter)
        
        # Número de guía
        numero_guia_label = QLabel("Número de Guía:")
        numero_guia_label.setFixedWidth(120)
        self.numero_guia_entry = QLineEdit()
        self.numero_guia_entry.setFixedWidth(200)
        self.numero_guia_entry.setPlaceholderText("Número de guía aquí...")
        
        # Nombre de empresa
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
        guia_empresa_fecha_layout.setContentsMargins(0, 20, 0, 20)
        main_content_layout.addLayout(guia_empresa_fecha_layout)

        # Layout para cantidad de productos, archivos de factura y guía
        productos_factura_guia_layout = QHBoxLayout()
        productos_factura_guia_layout.setAlignment(Qt.AlignHCenter)
        
        # Cantidad de productos
        cantidad_productos_label = QLabel("Cantidad de Productos:")
        cantidad_productos_label.setFixedWidth(120)
        self.cantidad_productos_entry = QLineEdit()
        self.cantidad_productos_entry.setFixedWidth(200)
        self.cantidad_productos_entry.setPlaceholderText("Números entre 1 y 99")
        
        # Archivo de factura
        factura_label = QLabel("Archivo Factura:")
        factura_label.setFixedWidth(120)
        self.factura_file_label = QLabel("")
        subir_factura_button = QPushButton("Subir archivo")
        subir_factura_button.setFixedWidth(150)
        subir_factura_button.clicked.connect(self.upload_factura)
        
        # Archivo de guía
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
        productos_factura_guia_layout.setContentsMargins(0, 20, 0, 20)
        main_content_layout.addLayout(productos_factura_guia_layout)

        # Layout para los nombres de archivos
        file_labels_layout = QHBoxLayout()
        file_labels_layout.setAlignment(Qt.AlignHCenter)
        self.factura_file_label.setStyleSheet("padding: 5px;")
        self.guia_file_label.setStyleSheet("padding: 5px;")
        file_labels_layout.addWidget(self.factura_file_label)
        file_labels_layout.addWidget(self.guia_file_label)
        file_labels_layout.setContentsMargins(20, 20, 20, 20)
        main_content_layout.addLayout(file_labels_layout)

        # Layout para los botones de cancelar y continuar justificados hacia abajo
        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        cancelar_button = QPushButton("Cancelar")
        cancelar_button.setFixedWidth(150)
        cancelar_button.setStyleSheet("""
            background-color: #FE6E0C;
            color: white;
            padding: 10px;
            border-radius: 5px;
        """)
        cancelar_button.clicked.connect(self.cancelar)
        aceptar_button = QPushButton("Continuar")
        aceptar_button.setFixedWidth(150)
        aceptar_button.setStyleSheet("""
            background-color: #FE6E0C;
            color: white;
            padding: 10px;
            border-radius: 5px;
        """)
        aceptar_button.clicked.connect(self.continuar_ingreso)
        
        # Añadir botones al layout
        buttons_layout.addWidget(cancelar_button)
        buttons_layout.addWidget(aceptar_button)

        # Añadir los layouts al layout principal
        main_layout.addLayout(title_layout)
        main_layout.addLayout(main_content_layout)
        main_layout.addLayout(buttons_layout)

        # Asignar el layout principal a la ventana
        self.setLayout(main_layout)

    def validar_existencia_archivos(self, guia_filename, factura_filename):
        guia_path = os.path.join("documents", "guia", guia_filename) if guia_filename else None
        factura_path = os.path.join("documents", "factura", factura_filename) if factura_filename else None

        if guia_filename and os.path.exists(guia_path):
            return f"El archivo {guia_filename} ya se encontró en el sistema, intenta con otro"
        elif factura_filename and os.path.exists(factura_path):
            return f"El archivo {factura_filename} ya se encontró en el sistema, intenta con otro"
        else:
            return None

    def validar_ingreso(self):
        cantidad_texto = self.cantidad_productos_entry.text().strip()

        # Validar que todos los campos estén llenos
        if (not self.numero_guia_entry.text().strip() or
            not self.nombre_empresa_entry.text().strip() or
            not self.fecha_picker.date().isValid() or
            not cantidad_texto or
            not self.factura_file_label.text().strip() or
            not self.guia_file_label.text().strip()):
            QMessageBox.warning(self, "Error", "Llene todos los campos")
            return False

        # Validar la fecha
        if self.fecha_picker.date().toPyDate() < QDate(2022, 1, 1).toPyDate():
            QMessageBox.warning(self, "Error", "Fecha ingresada incorrecta")
            return False

        # Validar la cantidad de productos
        if not cantidad_texto.isdigit() or not (1 <= int(cantidad_texto) <= 99):
            QMessageBox.warning(self, "Error", "Ingrese un número correcto en la cantidad de productos")
            return False

        # Validar si se han subido guía y factura
        if self.factura_file_label.text() == self.guia_file_label.text():
            QMessageBox.warning(self, "Error", "Guía y factura deben ser diferentes")
            return False

        return True

    def continuar_ingreso(self):
        # Validar ingreso antes de continuar
        if not self.validar_ingreso():
            return

        # Obtener nombres de archivos
        guia_filename = os.path.basename(self.guia_filename) if hasattr(self, 'guia_filename') else None
        factura_filename = os.path.basename(self.factura_filename) if hasattr(self, 'factura_filename') else None

        # Validar existencia de archivos
        error_message = self.validar_existencia_archivos(guia_filename, factura_filename)

        if error_message:
            QMessageBox.warning(self, "Error", error_message)
            return

        # Continuar con el proceso de ingreso
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
        data_manager = DataManager.get_instance()
        data_manager.limpiar_datos()
        self.controller.mostrar_opciones()
        
    def cargar_datos(self):
        numero_guia = self.data_manager.obtener_numero_guia()
        nombre_empresa = self.data_manager.obtener_nombre_empresa()
        fecha = self.data_manager.obtener_fecha()
        cantidad_productos = self.data_manager.obtener_cantidad_productos()

        if numero_guia:
            self.numero_guia_entry.setText(numero_guia)
        if nombre_empresa:
            self.nombre_empresa_entry.setText(nombre_empresa)
        if fecha:
            self.fecha_picker.setDate(QDate.fromString(fecha, "dd/MM/yyyy"))
        if cantidad_productos:
            self.cantidad_productos_entry.setText(cantidad_productos)
