import tkinter as tk
from tkinter import ttk

class BuscarProductoView:

    def __init__(self, root, controller):
        # Inicializa la vista para buscar un producto.

        # Args:
        #     root (tk.Tk): La ventana principal de la aplicación.
        #     controller (object): El controlador de la aplicación.
        self.root = root
        self.controller = controller
        self.root.title("Buscar Producto")

        # Agregar título
        self.titulo_label = tk.Label(self.root, text="Buscar Producto", font=("Arial", 14))
        self.titulo_label.pack(pady=10)

        # Agregar barra de búsqueda
        self.search_entry = tk.Entry(self.root, width=50)
        self.search_entry.pack(pady=10)

        # Agregar tabla
        self.tabla_frame = tk.Frame(self.root)
        self.tabla_frame.pack(fill="both", expand=True)

        self.scroll_frame = tk.Frame(self.tabla_frame)
        self.scroll_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.scroll_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas)
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Agregar encabezados de la tabla
        self.mostrar_label_tabla("Nombre", 0, 0)
        self.mostrar_label_tabla("Descripción", 1, 0)
        self.mostrar_label_tabla("Series", 2, 0)

        # Agregar filas de la tabla (ejemplo)
        for i in range(1, 4):
            self.mostrar_label_tabla(f"Producto {i}", 0, i)
            self.mostrar_label_tabla(f"Descripción del producto {i}", 1, i)
            self.mostrar_label_tabla(f"Serie 1, Serie 2", 2, i)

        # Agregar botón para volver a opciones
        self.volver_button = tk.Button(self.root, text="Volver a Opciones", command=self.volver_a_opciones)
        self.volver_button.pack(pady=10)

    def mostrar_label_tabla(self, text, columna, fila):
        """
        Muestra una etiqueta en la tabla.

        Args:
            text (str): El texto de la etiqueta.
            columna (int): La columna de la etiqueta.
            fila (int): La fila de la etiqueta.
        """
        label = tk.Label(self.inner_frame, text=text)
        label.grid(column=columna, row=fila, pady=5)

    def mostrar_buscar_producto(self):
        """
        Muestra la vista para buscar un producto.
        """
        self.root.mainloop()

    def volver_a_opciones(self):
        """
        Oculta la vista para buscar un producto y muestra la vista de opciones.
        """
        self.root.withdraw()
        self.controller.mostrar_opciones()

# Puedes agregar más lógica y elementos según tus necesidades

if __name__ == "__main__":
    buscar_producto_root = tk.Tk()
    buscar_producto_view = BuscarProductoView(buscar_producto_root, None)  # Se eliminó el espacio en blanco no imprimible
    buscar_producto_view.mostrar_buscar_producto()
