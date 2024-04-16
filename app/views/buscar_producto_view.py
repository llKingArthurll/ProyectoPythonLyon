<<<<<<< HEAD
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
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
        layout_principal = QtWidgets.QVBoxLayout()
        layout_principal.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.setLayout(layout_principal)

        layout_titulo = QtWidgets.QHBoxLayout()
        titulo_label = QtWidgets.QLabel("Busca tu producto aquí")
        titulo_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        layout_titulo.addWidget(titulo_label)
        layout_principal.addLayout(layout_titulo)

        layout_busqueda = QtWidgets.QHBoxLayout()
        self.barra_busqueda = QtWidgets.QLineEdit()
        self.barra_busqueda.setPlaceholderText("Buscar producto...")
        self.barra_busqueda.setFixedWidth(800)
        layout_busqueda.addWidget(self.barra_busqueda)
        
        boton_buscar = QtWidgets.QPushButton("Buscar")
        boton_buscar.setFixedWidth(150)
        boton_buscar.clicked.connect(self.buscar)
        layout_busqueda.addWidget(boton_buscar)
        
        boton_borrar = QtWidgets.QPushButton("Borrar")
        boton_borrar.setFixedWidth(150)
        boton_borrar.clicked.connect(self.borrar)
        layout_busqueda.addWidget(boton_borrar)
        
        layout_centrado_busqueda = QtWidgets.QHBoxLayout()
        layout_centrado_busqueda.addLayout(layout_busqueda)
        layout_principal.addLayout(layout_centrado_busqueda)

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
            
            # Crear texto con enlaces para Guía y Factura
            enlace_guia = QtWidgets.QTableWidgetItem("Ver guía")
            enlace_factura = QtWidgets.QTableWidgetItem("Ver factura")

            # Añadir señales a los enlaces para abrir los archivos PDF
            enlace_guia.setForeground(QtCore.Qt.blue)
            enlace_factura.setForeground(QtCore.Qt.blue)
            
            # Establecer que las celdas sean seleccionables para detectar clics
            self.tabla.setItem(i, 5, enlace_guia)
            enlace_guia.setFlags(enlace_guia.flags() | QtCore.Qt.ItemIsSelectable)
            
            self.tabla.setItem(i, 6, enlace_factura)
            enlace_factura.setFlags(enlace_factura.flags() | QtCore.Qt.ItemIsSelectable)
            
            # Conectar los enlaces a la función para abrir archivos
            enlace_guia.setData(QtCore.Qt.UserRole, (registro[0], "guia"))
            enlace_factura.setData(QtCore.Qt.UserRole, (registro[0], "factura"))
            enlace_guia.clicked.connect(self.abrir_pdf)
            enlace_factura.clicked.connect(self.abrir_pdf)

    def abrir_pdf(self):
        enlace = self.sender()
        id_nuevo_ingreso, tipo_archivo = enlace.data(QtCore.Qt.UserRole)
        
        # Obtener la ruta de la guía o factura según corresponda
        if tipo_archivo == "guia":
            ruta = self.db_queries.obtener_ruta_guia_por_id(id_nuevo_ingreso)
        else:
            ruta = self.db_queries.obtener_ruta_factura_por_id(id_nuevo_ingreso)
        
        # Abrir el PDF en la ruta especificada
        if ruta:
            os.startfile(ruta)
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", f"No se encontró ruta para {tipo_archivo}.")

    def abrir_ventana_seleccion(self):
        seleccion = self.tabla.selectedItems()
        if seleccion:
            fila_seleccionada = seleccion[0].row()
            if fila_seleccionada >= 0:
                id_nuevo_ingreso = self.tabla.item(fila_seleccionada, 0).text()
                self.controller.mostrar_buscar_serie(id_nuevo_ingreso)

    def set_controller(self, controller):
        self.controller = controller
=======
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.data.db_connection import DatabaseConnection
from app.data.db_queries import DatabaseQueries
from app.views.buscar_producto_especifico_view import BuscarProductoEspecificoView

class BuscarProductoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Buscar Producto")
        self.root.geometry("800x600")

        # Conexión a la base de datos
        self.db_queries = DatabaseQueries(DatabaseConnection())
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

    def buscar(self):
        QtWidgets.QMessageBox.information(self, "Información", "Botón 'buscar' activado")

<<<<<<< HEAD
    def borrar(self):
        QtWidgets.QMessageBox.information(self, "Información", "Botón 'borrar' activado")
=======
        # Frame para el cuadro de búsqueda y los botones
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        # Agregar cuadro de búsqueda con borde redondeado y color de borde blanco
        self.search_entry = tk.Entry(search_frame, width=30, font=("Arial", 11))
        self.search_entry.grid(row=0, column=0, padx=20)

        # Agregar botón de búsqueda
        self.search_button = tk.Button(search_frame, text="Buscar", command=self.buscar_en_tabla)
        self.search_button.grid(row=0, column=1, padx=10)

        # Agregar botón de borrar
        self.clear_button = tk.Button(search_frame, text="Borrar", command=self.borrar_tabla)
        self.clear_button.grid(row=0, column=2, padx=10)

        # Agregar tabla
        tabla_frame = tk.Frame(self.root, padx=20, pady=20)
        tabla_frame.pack(expand=True)

        self.tabla = ttk.Treeview(tabla_frame, columns=("ID", "Guía", "Empresa", "Cantidad", "Fecha"), show="headings")
        self.tabla.pack(expand=True, fill="both")

        # **Ajustar el ancho de las columnas**
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Guía", width=120, anchor="center")
        self.tabla.column("Empresa", width=250, anchor="center")
        self.tabla.column("Cantidad", width=100, anchor="center")
        self.tabla.column("Fecha", anchor="center")

        # Definir encabezados
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Guía", text="Guía")
        self.tabla.heading("Empresa", text="Empresa")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Fecha", text="Fecha")

        # Mostrar resumen de 'NuevoIngreso'
        self.mostrar_resumen_nuevoingreso()

        # Agregar botón para volver a opciones
        self.volver_button = tk.Button(self.root, text="Volver a Opciones", command=self.volver_a_opciones)
        self.volver_button.pack(side="bottom", pady=10)

        # Variable para almacenar ID seleccionado
        self.selected_id = None
        
        # Vincular el evento de presionar la tecla "Enter" con la función buscar_en_tabla
        self.search_entry.bind("<Return>", lambda event: self.buscar_en_tabla())

    def mostrar_resumen_nuevoingreso(self):
        resumen_nuevoingreso = self.db_queries.list_resumen_nuevoingreso()

        # Insertar datos
        for i, registro in enumerate(resumen_nuevoingreso, start=1):
            self.tabla.insert("", "end", values=(str(registro[0]), registro[1], registro[2], str(registro[3]), registro[4]))

        # Detectar selección de fila
        self.tabla.bind("<<TreeviewSelect>>", self.on_select_row)

    def mostrar_buscar_producto(self):
        self.root.mainloop()

    def volver_a_opciones(self):
        self.root.withdraw()
        self.controller.mostrar_opciones()

    def get_selected_id(self):
        # Obtener la selección actual
        selected_items = self.tabla.selection()
        
        # Verificar si hay alguna fila seleccionada
        if selected_items:
            # Si hay una fila seleccionada, obtener su ID
            selected_row = selected_items[0]
            selected_id = self.tabla.item(selected_row, "values")[0]
            return selected_id
        else:
            # Si no hay filas seleccionadas, devolver None o algún otro valor que indique que no hay selección
            return None


    def on_select_row(self, event):
        selected_id = self.get_selected_id()

        # Imprimir el ID seleccionado por consola
        print(f"ID seleccionado: {selected_id}")

        # Crear una nueva ventana para la vista "buscar_producto_especifico_view"
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title(f"Información del Producto - ID: {selected_id}")

        # Pasar el ID seleccionado a la nueva vista
        BuscarProductoEspecificoView(nueva_ventana, self.controller, selected_id)

    def buscar_en_tabla(self):
        # Obtener el texto de búsqueda
        texto_busqueda = self.search_entry.get()

        # Verificar si la caja de texto está vacía
        if not texto_busqueda.strip():
            messagebox.showwarning("Búsqueda vacía", "Su búsqueda está vacía.")
            return

        # Buscar primero por guía
        resultados_guia = self.db_queries.search_by_guia(texto_busqueda)
        if resultados_guia:
            print("Se encontró en la guía.")
            self.actualizar_tabla(resultados_guia)
            return

        # Buscar por empresa si no se encontró en la guía
        resultados_empresa = self.db_queries.search_by_empresa(texto_busqueda)
        if resultados_empresa:
            print("Se encontró en la empresa.")
            self.actualizar_tabla(resultados_empresa)
            return

        # Buscar por nombre de producto si no se encontró en la guía ni en la empresa
        resultados_producto = self.db_queries.search_by_nombre_producto(texto_busqueda)
        if resultados_producto:
            print("Se encontró en productos.")
            self.actualizar_tabla(resultados_producto)
            return

        # Buscar por serie si no se encontró en la guía, empresa ni en el nombre del producto
        resultados_serie = self.db_queries.search_by_serie(texto_busqueda)
        if resultados_serie:
            print("Se encontró en serie.")
            self.actualizar_tabla(resultados_serie)
            return

        # Si no se encontraron resultados en ninguno de los casos anteriores
        messagebox.showwarning("Búsqueda sin resultados", "No se encontraron resultados para la búsqueda realizada.")

    def actualizar_tabla(self, resultados):
        # Limpiar la tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Insertar datos
        for id_tuple in resultados:
            id_entero = int(id_tuple[0])
            # Obtener datos completos para el ID
            datos_completos = self.db_queries.obtener_datos_completos(id_entero)
            if datos_completos:
                # Insertar datos en la tabla
                self.tabla.insert("", "end", values=(id_entero, *datos_completos[0]))
                print(datos_completos)

    def borrar_tabla(self):
        # Limpiar la tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        
        # Limpiar el contenido de la caja de texto
        self.search_entry.delete(0, tk.END)
        
        # Mostrar resumen de 'NuevoIngreso'
        self.mostrar_resumen_nuevoingreso()
        
        # Dar foco al cuadro de búsqueda
        self.search_entry.focus_set()
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3
