from PyQt5 import QtWidgets, QtGui, QtCore
from app.data.db_queries import DatabaseQueries
import os

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
        # Configurar el layout principal
        layout_principal = QtWidgets.QVBoxLayout()
        self.setLayout(layout_principal)

        # Configurar el título centrado
        layout_titulo = QtWidgets.QHBoxLayout()
        layout_titulo.setAlignment(QtCore.Qt.AlignCenter)  # Centrar el título
        titulo_label = QtWidgets.QLabel("Busca tu producto aquí")
        titulo_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        layout_titulo.addWidget(titulo_label)
        layout_principal.addLayout(layout_titulo)

        # Configurar el layout para la barra de búsqueda
        layout_busqueda = QtWidgets.QHBoxLayout()
        self.barra_busqueda = QtWidgets.QLineEdit()
        self.barra_busqueda.setPlaceholderText("Buscar producto...")
        self.barra_busqueda.setFixedWidth(800)
        self.barra_busqueda.setFocus()  # Establecer foco en la barra de búsqueda
        layout_busqueda.addWidget(self.barra_busqueda)

        # Configurar el botón de buscar
        boton_buscar = QtWidgets.QPushButton("Buscar")
        boton_buscar.setFixedWidth(150)
        boton_buscar.clicked.connect(self.busqueda_especifica)
        boton_buscar.setStyleSheet("""
            background-color: #FE6E0C;
            color: white;
            padding: 10px;
            border-radius: 5px;
        """)
        layout_busqueda.addWidget(boton_buscar)
        
        # Asignar la acción de búsqueda a la tecla Enter en la barra de búsqueda
        self.barra_busqueda.returnPressed.connect(self.busqueda_especifica)
        
        # Configurar el botón de borrar
        boton_borrar = QtWidgets.QPushButton("Borrar")
        boton_borrar.setFixedWidth(150)
        boton_borrar.clicked.connect(self.borrar)
        boton_borrar.setStyleSheet("""
            background-color: #FE6E0C;
            color: white;
            padding: 10px;
            border-radius: 5px;
        """)
        layout_busqueda.addWidget(boton_borrar)

        # Añadir el layout de búsqueda al layout principal
        layout_principal.addLayout(layout_busqueda)

        # Configurar el layout para la tabla
        layout_centro = QtWidgets.QHBoxLayout()
        layout_centro.setAlignment(QtCore.Qt.AlignCenter)  # Centrar la tabla
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

        # Añadir un botón de "Volver" después de la tabla
        layout_volver = QtWidgets.QHBoxLayout()
        layout_volver.setAlignment(QtCore.Qt.AlignCenter)  # Centrar el botón "Volver"
        boton_volver = QtWidgets.QPushButton("Volver")
        boton_volver.setFixedWidth(150)
        boton_volver.clicked.connect(self.volver_opciones)  # Conecta la función a ejecutar al hacer clic
        boton_volver.setStyleSheet("""
            background-color: #FE6E0C;
            color: white;
            padding: 10px;
            border-radius: 5px;
        """)
        layout_volver.addWidget(boton_volver)
        layout_principal.addLayout(layout_volver)

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
        if tipo_archivo == "factura":
            ruta = self.db_queries.obtener_ruta_factura_por_id(id_nuevo_ingreso)
        else:
            ruta = self.db_queries.obtener_ruta_guia_por_id(id_nuevo_ingreso)
        
        # Verificar si la ruta es válida
        if ruta:
            print(f"Abrir archivo PDF: {ruta}")
            try:
                os.startfile(ruta)
            except Exception as e:
                print(f"Error al abrir el PDF: {e}")
                QtWidgets.QMessageBox.warning(self, "Advertencia", f"No se pudo abrir el archivo {tipo_archivo}.")
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", f"No se encontró ruta para {tipo_archivo}.")

    def abrir_ventana_seleccion(self):
        seleccion = self.tabla.selectedItems()
        if seleccion:
            fila_seleccionada = seleccion[0].row()
            if fila_seleccionada >= 0:
                id_nuevo_ingreso = self.tabla.item(fila_seleccionada, 0).text()
                self.controller.mostrar_buscar_serie(id_nuevo_ingreso)

    def busqueda_especifica(self):
        consulta = self.barra_busqueda.text().strip()
        
        # Inicializar una lista para almacenar IDs de resultados únicos
        ids_unicos = set()
        
        # Buscar por número de guía
        resultados_guia = self.db_queries.buscar_por_numero_guia(consulta)
        if resultados_guia:
            print("Se encontró en la guía")
            ids_unicos.update(resultados_guia)

        # Buscar por nombre de empresa
        resultados_empresa = self.db_queries.buscar_por_nombre_empresa(consulta)
        if resultados_empresa:
            print("Se encontró en nombre de empresa")
            ids_unicos.update(resultados_empresa)
        
        # Buscar por nombre de producto
        resultados_producto = self.db_queries.buscar_por_nombre_producto(consulta)
        if resultados_producto:
            print("Se encontró en nombre de producto")
            ids_unicos.update(resultados_producto)
        
        # Buscar por serie de producto
        resultados_serie = self.db_queries.buscar_por_serie_producto(consulta)
        if resultados_serie:
            print("Se encontró en la serie")
            ids_unicos.update(resultados_serie)
        
        # Convertir el conjunto de IDs únicos a una lista
        ids_unicos = list(ids_unicos)
        
        # Si no hay resultados, mostrar un mensaje
        if not ids_unicos:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se encontró nada en la búsqueda.")
            return
        
        # Si hay resultados, actualizar la tabla con los resultados únicos
        self.actualizar_tabla_por_ids(ids_unicos)

    def actualizar_tabla_por_ids(self, ids):
        # Limpiar la tabla actual
        self.tabla.clearContents()
        self.tabla.setRowCount(0)  # Restablecer el número de filas de la tabla

        # Verificar si hay ID para actualizar
        if not ids:
            print("No hay ID para actualizar.")
            return

        # Crear una lista para almacenar todos los datos que se obtengan por cada ID
        todos_los_datos = []

        # Recorrer los ID obtenidos de las búsquedas
        for id_nuevo_ingreso in ids:
            # Obtener los detalles del nuevo ingreso por ID
            detalles_ingreso = self.db_queries.obtener_nuevo_ingreso_por_id(id_nuevo_ingreso)
            if detalles_ingreso:
                todos_los_datos.append(detalles_ingreso)

        # Verificar si se obtuvieron datos
        if not todos_los_datos:
            print("No se obtuvieron datos para los ID dados.")
            return

        # Establecer el número de filas de la tabla según los datos obtenidos
        self.tabla.setRowCount(len(todos_los_datos))

        # Llenar la tabla con los datos obtenidos
        for i, datos in enumerate(todos_los_datos):
            for j, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tabla.setItem(i, j, item)

            # Obtener las rutas de la guía y la factura
            ruta_guia = self.db_queries.obtener_ruta_guia_por_id(datos[0])
            ruta_factura = self.db_queries.obtener_ruta_factura_por_id(datos[0])

            # Crear botones para ver Guía y Factura
            boton_guia = QtWidgets.QPushButton("Ver Guía")
            boton_guia.setStyleSheet("color: blue; text-decoration: underline;")
            boton_guia.clicked.connect(lambda _, idx=datos[0]: self.abrir_pdf(idx, "guia"))
            self.tabla.setCellWidget(i, 5, boton_guia)
            
            boton_factura = QtWidgets.QPushButton("Ver Factura")
            boton_factura.setStyleSheet("color: blue; text-decoration: underline;")
            boton_factura.clicked.connect(lambda _, idx=datos[0]: self.abrir_pdf(idx, "factura"))
            self.tabla.setCellWidget(i, 6, boton_factura)

    def borrar(self):
        self.barra_busqueda.clear()
        self.mostrar_datos_en_tabla()
        self.barra_busqueda.setFocus()
    
    def set_controller(self, controller):
        self.controller = controller
    
    def volver_opciones(self):
        self.close()
        self.controller.mostrar_opciones()
