import tkinter as tk
from tkinter import ttk, messagebox

class PantallaResumen:
    def __init__(self, root, numero_guia, nombre_empresa, fecha, cantidad_productos, file_name1, file_name2, productos_guardados):
        self.root = root
        self.numero_guia = numero_guia
        self.nombre_empresa = nombre_empresa
        self.fecha = fecha
        self.cantidad_productos = cantidad_productos
        self.file_name1 = file_name1
        self.file_name2 = file_name2
        self.productos_guardados = productos_guardados

        self.root.title("Resumen")
        self.root.geometry("500x650")
        self.root.resizable(False, False)  # Hace que la ventana no sea redimensionable

        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill="both", pady=20, padx=20)

        self.create_content()

    def create_content(self):
        title_label = ttk.Label(self.frame, text="Resumen de la Guía", font=("Helvetica", 20))
        title_label.pack(pady=20)

        guia_label = ttk.Label(self.frame, text=f"Número de Guía: {self.numero_guia}")
        guia_label.pack()

        empresa_label = ttk.Label(self.frame, text=f"Nombre de la Empresa: {self.nombre_empresa}")
        empresa_label.pack()

        fecha_label = ttk.Label(self.frame, text=f"Fecha: {self.fecha}")
        fecha_label.pack()

        cantidad_label = ttk.Label(self.frame, text=f"Cantidad de Productos: {self.cantidad_productos}")
        cantidad_label.pack()

        guia_filename_label = ttk.Label(self.frame, text=f"Nombre de la Guía: {self.file_name1}")
        guia_filename_label.pack()

        factura_filename_label = ttk.Label(self.frame, text=f"Nombre de la Factura: {self.file_name2}")
        factura_filename_label.pack()

        title_productos = ttk.Label(self.frame, text="Productos Guardados", font=("Helvetica", 16))
        title_productos.pack(pady=10)

        # Agregamos un Frame para contener los productos y un Scrollbar
        frame_productos = ttk.Frame(self.frame)
        frame_productos.pack(expand=True, fill="both")

        canvas = tk.Canvas(frame_productos)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_productos, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        ancho_label = 75

        for i, producto in enumerate(self.productos_guardados, start=1):
            producto_label = ttk.Label(inner_frame, text=f"--- Producto {i} ---", anchor="center", width=ancho_label)
            producto_label.pack(fill="both")

            nombre_label = ttk.Label(inner_frame, text=f"Nombre del Producto: {producto[0]}", anchor="center", width=ancho_label)
            nombre_label.pack(fill="both")

            descripcion_label = ttk.Label(inner_frame, text=f"Descripción del Producto: {producto[1]}", anchor="center", width=ancho_label)
            descripcion_label.pack(fill="both")

            series_label = ttk.Label(inner_frame, text=f"Series: {producto[2]}", anchor="center", width=ancho_label)
            series_label.pack(fill="both")

        inner_frame.update_idletasks()

        canvas.config(scrollregion=canvas.bbox("all"))

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        inner_frame.bind("<Configure>", on_configure)

        # Botones
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=20)

        cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.cancelar)
        cancel_button.pack(side="left", padx=10)

        guardar_button = ttk.Button(button_frame, text="Guardar", command=self.guardar)
        guardar_button.pack(side="right", padx=10)

    def cancelar(self):
        self.root.destroy()

    def guardar(self):
        messagebox.showinfo("Guardado", "La información ha sido guardada exitosamente.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaResumen(root, "123", "Empresa X", "01/01/2023", "5", "guia.pdf", "factura.pdf", [
        ("Producto1", "Descripción1", "Serie1"),
        ("Producto2", "Descripción2", "Serie2"),
        ("Producto3", "Descripción3", "Serie3"),
        ("Producto4", "Descripción4", "Serie4"),
        ("Producto5", "Descripción5", "Serie5")
    ])
    root.mainloop()
