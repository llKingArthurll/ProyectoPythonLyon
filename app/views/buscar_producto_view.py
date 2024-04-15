from PyQt5 import QtWidgets, QtGui, QtCore
from app.data.db_queries import DatabaseQueries
import subprocess

class BuscarProductoView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buscar Producto")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QtGui.QIcon("resources/LogoLyon.ico"))
        self.showMaximized()

        self.db_queries = DatabaseQueries()
        self.configurar_ui()

    def configurar_ui(self):
        layout_principal = QtWidgets.QVBoxLayout()
        layout_principal.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.setLayout(layout_principal)

        # Layout para el título
        layout_titulo = QtWidgets.QHBoxLayout()
        titulo_label = QtWidgets.QLabel("Busca tu producto aquí")
        titulo_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        layout_titulo.addWidget(titulo_label)
        layout_principal.addLayout(layout_titulo)

        # Layout para la barra de búsqueda
        layout_busqueda = QtWidgets.QHBoxLayout()
        self.barra_busqueda = QtWidgets.QLineEdit()
        self.barra_busqueda.setPlaceholderText("Buscar producto...")
        self.barra_busqueda.setFixedWidth(800)
        layout_busqueda.addWidget(self.barra_busqueda)
        
        # Botón de buscar
        boton_buscar = QtWidgets.QPushButton("Buscar")
        boton_buscar.setFixedWidth(150)
        boton_buscar.clicked.connect(self.buscar)
        layout_busqueda.addWidget(boton_buscar)
        
        # Botón de borrar
        boton_borrar = QtWidgets.QPushButton("Borrar")
        boton_borrar.setFixedWidth(150)
        boton_borrar.clicked.connect(self.borrar)
        layout_busqueda.addWidget(boton_borrar)
        
        layout_centrado_busqueda = QtWidgets.QHBoxLayout()
        layout_centrado_busqueda.addLayout(layout_busqueda)
        layout_principal.addLayout(layout_centrado_busqueda)

        # Layout para la tabla
        layout_centro = QtWidgets.QHBoxLayout()
        layout_centro.setAlignment(QtCore.Qt.AlignCenter)
        self.tabla = QtWidgets.QTableWidget()
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre Guía", "Nombre Empresa", "Cantidad Productos", "Fecha Guía", "Guía", "Factura"])
        self.tabla.setMinimumWidth(600)
        self.tabla.setMinimumHeight(400)
        self.tabla.setMaximumWidth(1250)
        self.tabla.setMaximumHeight(2000)
        self.tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        layout_centro.addWidget(self.tabla)
        layout_principal.addLayout(layout_centro)
        
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.itemSelectionChanged.connect(self.abrir_ventana_seleccion)
        self.mostrar_datos_en_tabla()

    def mostrar_datos_en_tabla(self):
        resumen_nuevo_ingreso = self.db_queries.obtener_resumen_nuevo_ingreso()
        if not resumen_nuevo_ingreso:
            print("No se encontraron datos en la base de datos.")
            return
        
        self.tabla.setRowCount(len(resumen_nuevo_ingreso))

        for i, registro in enumerate(resumen_nuevo_ingreso):
            for j, valor in enumerate(registro):
                item = QtWidgets.QTableWidgetItem(str(valor))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tabla.setItem(i, j, item)

            # Obtener las rutas de la guía y la factura
            ruta_guia = self.db_queries.obtener_ruta_guia_por_id(registro[0])
            ruta_factura = self.db_queries.obtener_ruta_factura_por_id(registro[0])

            # Crear botones para ver Guía y Factura
            boton_guia = QtWidgets.QPushButton("Ver Guía")
            boton_guia.setStyleSheet("color: blue; text-decoration: underline;")
            boton_guia.clicked.connect(lambda _, idx=registro[0]: self.abrir_pdf(idx, "guia"))
            self.tabla.setCellWidget(i, 5, boton_guia)
            
            boton_factura = QtWidgets.QPushButton("Ver Factura")
            boton_factura.setStyleSheet("color: blue; text-decoration: underline;")
            boton_factura.clicked.connect(lambda _, idx=registro[0]: self.abrir_pdf(idx, "factura"))
            self.tabla.setCellWidget(i, 6, boton_factura)

    def abrir_pdf(self, id_nuevo_ingreso, tipo_archivo):
        # Obtener la ruta del PDF según el tipo de archivo
        if tipo_archivo == "guia":
            ruta = self.db_queries.obtener_ruta_guia_por_id(id_nuevo_ingreso)
        else:
            ruta = self.db_queries.obtener_ruta_factura_por_id(id_nuevo_ingreso)
        
        # Imprimir la ruta en la consola
        print(f"Ruta del archivo {tipo_archivo}: {ruta}")

        # La función solo imprime la ruta por consola; no intenta abrir el archivo PDF.


    def abrir_ventana_seleccion(self):
        seleccion = self.tabla.selectedItems()
        if seleccion:
            fila_seleccionada = seleccion[0].row()
            if fila_seleccionada >= 0:
                id_nuevo_ingreso = self.tabla.item(fila_seleccionada, 0).text()
                self.controller.mostrar_buscar_serie(id_nuevo_ingreso)

    def set_controller(self, controller):
        self.controller = controller

    def buscar(self):
        QtWidgets.QMessageBox.information(self, "Información", "Botón 'buscar' activado")

    def borrar(self):
        QtWidgets.QMessageBox.information(self, "Información", "Botón 'borrar' activado")
