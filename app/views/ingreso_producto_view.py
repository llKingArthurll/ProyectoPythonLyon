import tkinter as tk
from app.data.data_manager import DataManager
from app.views.agregar_serie_view import AgregarSerieView

class IngresoProductoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.agregar_serie_view_window = None
        self.root.title("Ingreso de Producto")
        self.root.geometry("615x500")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="¡Bienvenido al ingreso de productos!")
        self.label.pack(pady=20)

        self.data_manager = DataManager()
        cantidad_productos = self.data_manager.get_cantidad_productos()

        cantidad_label = tk.Label(root, text=f"Cantidad de productos: {cantidad_productos}")
        cantidad_label.pack(pady=10)

        self.entry_series_dict = {}
        self.productos = []

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

    def mostrar_ingreso_producto(self):
        self.root.mainloop()

    def cancelar(self):
        self.root.withdraw()
        self.controller.mostrar_ingresar_nuevo()

    def create_content(self):
        for i in range(1, int(self.data_manager.get_cantidad_productos()) + 1):
            frame_product = tk.Frame(self.frame, padx=0, pady=10)
            frame_product.pack(anchor="w", pady=(0, 10), fill="x")

            label1 = tk.Label(frame_product, text=f"Producto {i}:", anchor="e")
            label1.grid(row=0, column=0, sticky="w", padx=(15, 5))

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

            button_agregar_serie = tk.Button(frame_product, text="Agregar Serie", command=lambda i=i, entry_series=entry_series: self.abrir_agregar_serie_view(entry_series), width=14)
            button_agregar_serie.grid(row=2, column=2, padx=(5, 10), pady=(5, 5))

            button_reestablecer_serie = tk.Button(frame_product, text="Reestablecer Serie", command=lambda entry_series=entry_series: self.reestablecer_serie(entry_series), width=14)
            button_reestablecer_serie.grid(row=3, column=2, padx=(5, 10), pady=(5, 5))

            self.entry_series_dict[i] = entry_series
            self.productos.append((entry2, entry3, entry_series))

        self.cancelar_button = tk.Button(self.frame, text="Cancelar", command=self.cancelar)
        self.cancelar_button.pack(pady=10, side="left", anchor="center")

        self.continuar_button = tk.Button(self.frame, text="Continuar", command=self.mostrar_resumen_view)
        self.continuar_button.pack(pady=10, side="right", anchor="center")

    def reestablecer_serie(self, entry_series):
        entry_series.config(state="normal")
        entry_series.delete(0, tk.END)
        entry_series.insert(0, "")
        entry_series.config(state="readonly")

    def abrir_agregar_serie_view(self, entry_series):
        if not self.agregar_serie_view_window or not self.agregar_serie_view_window.winfo_exists():
            self.agregar_serie_view_window = tk.Toplevel(self.root)
            agregar_serie_view = AgregarSerieView(self.agregar_serie_view_window, entry_series, self)

    def mostrar_resumen_view(self):
        print("Pasando los datos al resumen...")
