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
        self.root.iconbitmap("resources/LogoLyon.ico")
        
        # Conexión a la base de datos
        self.db_queries = DatabaseQueries(DatabaseConnection())

        # Agregar título
        self.titulo_label = tk.Label(self.root, text="Buscar Producto", font=("Arial", 14))
        self.titulo_label.pack(pady=10)

        # Frame para el cuadro de búsqueda y los botones
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        # Agregar cuadro de búsqueda con borde redondeado y color de borde blanco
        self.search_entry = tk.Entry(search_frame, width=30, font=("Arial", 11))
        self.search_entry.grid(row=0, column=0, padx=20)

        # Agregar botón de búsqueda
        self.search_button = tk.Button(search_frame, text="Buscar", command=self.buscar_en_tabla, bg="#6287A2",fg="white", height=2, width=10, font=("Arial", 9))
        self.search_button.grid(row=0, column=1, padx=10)

        # Agregar botón de borrar
        self.clear_button = tk.Button(search_frame, text="Borrar", command=self.borrar_tabla, bg="#6287A2",fg="white", height=2, width=10, font=("Arial", 9))
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
        self.volver_button = tk.Button(self.root, text="Volver a Opciones", command=self.volver_a_opciones, bg="#FE6E0C",fg="white", height=2, width=20, font=("Arial", 9))
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

        # Verificar si se ha seleccionado una fila
        if selected_id is not None:
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
