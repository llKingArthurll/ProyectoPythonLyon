import tkinter as tk
from tkinter import ttk, messagebox
from miapp.pantalla_agregar_serie import PantallaAgregarSerie
from miapp.pantalla_resumen import PantallaResumen


class PantallaAgregarProductos:
    def __init__(self, root, numero_guia, nombre_empresa, fecha, cantidad_productos, file_name1, file_name2, pantalla_formulario):
        self.root = root
        self.pantalla_formulario = pantalla_formulario
        self.numero_guia = numero_guia
        self.nombre_empresa = nombre_empresa
        self.fecha = fecha
        self.cantidad_productos = cantidad_productos
        self.file_name1 = file_name1
        self.file_name2 = file_name2
        self.productos = []
        self.entry_series_dict = {}
        self.pantalla_agregar_serie_window = None
        self.root.title("Agregar Productos")
        self.root.geometry("615x500")

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.root, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.create_content()

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_content(self):
        title_label = tk.Label(self.frame, text="Agrega tu(s) producto(s)", anchor="w")
        title_label.pack(fill="x", padx=10, pady=(10, 0))

        for i in range(1, int(self.cantidad_productos) + 1):
            frame_product = tk.Frame(self.frame, padx=10, pady=10)
            frame_product.pack(anchor="w", pady=(0, 10))

            label1 = tk.Label(frame_product, text=f"Producto {i}:", anchor="e")
            label1.grid(row=0, column=0, sticky="w")

            label2 = tk.Label(frame_product, text="Nombre del producto:", anchor="e")
            label2.grid(row=1, column=0, sticky="w", padx=(50, 5), pady=(5, 5))

            entry2 = tk.Entry(frame_product, width=40)
            entry2.grid(row=1, column=1, padx=(5, 10), pady=(5, 5))
            entry2.insert(0, "Ingrese nombre")

            label3 = tk.Label(frame_product, text="Descripción del producto:", anchor="e")
            label3.grid(row=2, column=0, sticky="w", padx=(50, 5), pady=(5, 5))

            entry3 = tk.Entry(frame_product, width=40)
            entry3.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))
            entry3.insert(0, "Ingrese descripción")

            label4 = tk.Label(frame_product, text="Series:", anchor="e")
            label4.grid(row=3, column=0, sticky="w", padx=(50, 5), pady=(5, 5))

            entry_series = tk.Entry(frame_product, width=40, state="readonly")
            entry_series.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))
            entry_series.insert(0, "Ingrese series")

            button_agregar_serie = tk.Button(frame_product, text="Agregar Serie", command=lambda i=i, entry_series=entry_series: self.abrir_pantalla_agregar_serie(entry_series), width=14)
            button_agregar_serie.grid(row=2, column=2, padx=(5, 10), pady=(5, 5))

            button_reestablecer_serie = tk.Button(frame_product, text="Reestablecer Serie", command=lambda entry_series=entry_series: self.reestablecer_serie(entry_series), width=14)
            button_reestablecer_serie.grid(row=3, column=2, padx=(5, 10), pady=(5, 5))

            self.entry_series_dict[i] = entry_series
            self.productos.append((entry2, entry3, entry_series))

        button_frame = tk.Frame(self.frame)
        button_frame.pack(fill="x", padx=10, pady=(20, 10), anchor="e")

        cancel_button = tk.Button(button_frame, text="Cancelar", command=self.cancel, width=10)
        cancel_button.pack(side="left", padx=10)

        save_button = tk.Button(button_frame, text="Guardar", command=self.save, width=10)
        save_button.pack(side="right", padx=10)

    def abrir_pantalla_agregar_serie(self, entry_series):
        if not self.pantalla_agregar_serie_window or not self.pantalla_agregar_serie_window.winfo_exists():
            self.pantalla_agregar_serie_window = tk.Toplevel(self.root)
            pantalla_agregar_serie = PantallaAgregarSerie(self.pantalla_agregar_serie_window, entry_series, self)

    def reestablecer_serie(self, entry_series):
        entry_series.config(state="normal")
        entry_series.delete(0, tk.END)
        entry_series.insert(0, "")
        entry_series.config(state="readonly")

    def cancel(self):
        self.root.withdraw()
        self.pantalla_formulario.root.deiconify()

    def save(self):
        productos_guardados = []
        for i, producto in enumerate(self.productos, start=1):
            nombre_producto = producto[0].get()
            descripcion_producto = producto[1].get()
            series_producto = producto[2].get()
            productos_guardados.append((nombre_producto, descripcion_producto, series_producto))
        
        # Impresión de valores para saber como se están pasando
        print("----- Resumen en consola -------")
        print(f"Número de guía: {self.numero_guia}")
        print(f"Nombre de la empresa: {self.nombre_empresa}")
        print(f"Fecha: {self.fecha}")
        print(f"Canridad de productos: {self.cantidad_productos}")
        print(f"Nombre del pdf 1: {self.file_name1}")
        print(f"Nombre del pdf 2: {self.file_name2}")
        print("--------------------------------")
        
        self.root.withdraw()

        pantalla_resumen_window = tk.Toplevel(self.pantalla_formulario.root)
        pantalla_resumen = PantallaResumen(
            pantalla_resumen_window,
            self.numero_guia,
            self.nombre_empresa,
            self.fecha,
            self.cantidad_productos,
            self.file_name1,
            self.file_name2,
            productos_guardados,
            self.pantalla_formulario
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAgregarProductos(root, "123", "Empresa X", "01/01/2023", "2", "guia.pdf", "factura.pdf", None)
    root.mainloop()
