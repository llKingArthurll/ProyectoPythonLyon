import tkinter as tk
from tkinter import ttk

from app.data.db_connection import DatabaseConnection
from app.data.db_queries import DatabaseQueries

class BuscarProductoEspecificoView:
    def __init__(self, root, controller, selected_id):
        self.root = root
        self.controller = controller
        self.selected_id = selected_id
        self.root.geometry("600x600")

        # Mostrar el ID seleccionado en un Label
        self.titulo_label = tk.Label(self.root, text=f"ID del Producto: {self.selected_id}", font=("Arial", 14))
        self.titulo_label.pack(expand=True, pady=10)

        # Frame para la tabla
        tabla_frame = tk.Frame(self.root)
        tabla_frame.pack(expand=True)

        # Conexión a la base de datos
        db_connection = DatabaseConnection()
        db_queries = DatabaseQueries(db_connection)

        # Obtener información del producto
        nombre_producto = db_queries.search_products_by_id_nombre(self.selected_id)
        descripcion_producto = db_queries.search_products_by_id_descripcion(self.selected_id)
        series_producto = db_queries.search_products_by_id_serie(self.selected_id)

        # Convertir las cadenas a arreglos
        productos = nombre_producto.split(",")
        descripciones = descripcion_producto.split(",")
        series = series_producto.split(",")

        # Mostrar la información del producto en una tabla
        tabla = ttk.Treeview(tabla_frame, columns=("Nombre", "Descripción", "Series"), show="headings")
        tabla.pack(expand=True, fill="both")

        # Ajustar el ancho de las columnas
        tabla.column("#1", width=150, minwidth=0, stretch=False)  # Comienza desde la columna 1
        tabla.column("#2", width=100)
        tabla.column("#3", width=150)

        # Mostrar encabezados desde la primera columna
        tabla.heading("#1", text="Nombre", anchor="center")  # Comienza desde la columna 1
        tabla.heading("#2", text="Descripción", anchor="center")
        tabla.heading("#3", text="Series", anchor="center")

        # Insertar datos en la tabla (fila por fila)
        for i, (nombre, descripcion, serie) in enumerate(zip(productos, descripciones, series), start=1):
            tabla.insert("", "end", values=(nombre, descripcion, serie))

        # Centrar la tabla en el frame
        tabla_frame.pack(expand=True, pady=20)

        # Centrar el contenido de las celdas
        for j in range(1, 4):  # Comienza desde la columna 1
            tabla.column(f"#{j}", width=150, anchor="center")  # Aquí puedes modificar el tamaño de cada columna de la tabla
