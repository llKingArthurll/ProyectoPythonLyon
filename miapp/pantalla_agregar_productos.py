import tkinter as tk

class PantallaAgregarProductos:
    def __init__(self, root, cantidad_productos):
        self.root = root
        self.root.title("Agregar Productos")
        # Configurar el ancho y alto de la ventana (600x500)
        self.root.geometry("600x500")

        self.cantidad_productos = cantidad_productos

        # Crear un Canvas para agregar el contenido con scrollbars
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Agregar un scrollbar vertical
        scrollbar = tk.Scrollbar(self.root, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un frame interior para el contenido
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.create_content()

        # Configurar el canvas para el desplazamiento
        self.frame.update_idletasks()  # Asegurar que el frame tiene un tamaño adecuado
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Agregar controlador de eventos para la rueda del ratón
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_content(self):
        # Título antes del primer label
        title_label = tk.Label(self.frame, text="Agrega tu(s) producto(s)", anchor="w")
        title_label.pack(fill="x", padx=10, pady=(10, 0))

        for i in range(1, int(self.cantidad_productos) + 1):
            # En lugar de agregar a self.root, agregamos al frame interior (frame)
            frame_product = tk.Frame(self.frame, padx=10, pady=10)  # Agregar espacio alrededor
            frame_product.pack(anchor="w", pady=(0, 10))

            label1 = tk.Label(frame_product, text=f"Producto {i}:", anchor="e")
            label1.grid(row=0, column=0, sticky="w")

            label2 = tk.Label(frame_product, text="Nombre del producto:", anchor="e")
            label2.grid(row=1, column=0, sticky="w", padx=(50, 5), pady=(5, 5))  # Espacio a la izquierda y arriba/abajo

            entry2 = tk.Entry(frame_product, width=40)
            entry2.grid(row=1, column=1, padx=(5, 10), pady=(5, 5))  # Espacio a la derecha y arriba/abajo

            label3 = tk.Label(frame_product, text="Descripción del producto:", anchor="e")
            label3.grid(row=2, column=0, sticky="w", padx=(50, 5), pady=(5, 5))  # Espacio a la izquierda y arriba/abajo

            entry3 = tk.Entry(frame_product, width=40)
            entry3.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))  # Espacio a la derecha y arriba/abajo

            label4 = tk.Label(frame_product, text="Series:", anchor="e")
            label4.grid(row=3, column=0, sticky="w", padx=(50, 5), pady=(5, 5))  # Espacio a la izquierda y arriba/abajo

            entry4 = tk.Entry(frame_product, width=40)
            entry4.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))  # Espacio a la derecha y arriba/abajo

        # Botones Cancelar y Guardar
        button_frame = tk.Frame(self.frame)
        button_frame.pack(fill="x", padx=10, pady=(20, 10), anchor="e")

        cancel_button = tk.Button(button_frame, text="Cancelar", command=self.cancel)
        cancel_button.pack(side="left", padx=10)

        save_button = tk.Button(button_frame, text="Guardar", command=self.save)
        save_button.pack(side="right", padx=10)

    def cancel(self):
        self.root.destroy()

    def save(self):
        print(f"Cantidad de productos: {self.cantidad_productos}")

        for i in range(1, int(self.cantidad_productos) + 1):
            nombre_producto = self.frame.winfo_children()[i].winfo_children()[4].get()  # Usar el índice correcto (4)
            descripcion_producto = self.frame.winfo_children()[i].winfo_children()[7].get()  # Usar el índice correcto (7)
            series = self.frame.winfo_children()[i].winfo_children()[10].get()  # Usar el índice correcto (10)

            print(f"Producto {i}:")
            print(f"Nombre del producto: {nombre_producto}")
            print(f"Descripción del producto: {descripcion_producto}")
            print(f"Series: {series}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAgregarProductos(root, 10)
    root.mainloop()
