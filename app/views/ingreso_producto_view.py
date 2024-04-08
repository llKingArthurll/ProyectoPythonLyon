from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class IngresoProductoView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Producto")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        title_label = QLabel("Ingrese un producto aquí")
        layout.addWidget(title_label)
        self.setLayout(layout)



# import tkinter as tk
# from app.data.data_manager import DataManager
# from app.views.agregar_serie_view import AgregarSerieView

# class IngresoProductoView:
#     def __init__(self, root, controller):
#         self.root = root
#         self.controller = controller
#         self.agregar_serie_view_window = None
#         self.root.title("Ingreso de Producto")
#         self.root.geometry("615x500")
#         self.root.resizable(False, False)
#         self.root.iconbitmap("resources/LogoLyon.ico")

#         self.label = tk.Label(root, text="Ingresa los datos de los productos", font=("Arial", 15, "bold"))
#         self.label.pack(pady=20)

#         self.data_manager = DataManager()
#         cantidad_productos = self.data_manager.get_cantidad_productos()

#         cantidad_label = tk.Label(root, text=f"Cantidad de productos: {cantidad_productos}", font=("Arial", 12, "bold"))
#         cantidad_label.pack(pady=10)

#         self.frame = tk.Frame(self.root)
#         self.frame.pack(fill="both", expand=True)

#         self.canvas = tk.Canvas(self.frame)
#         self.canvas.pack(side="left", fill="both", expand=True)

#         self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
#         self.scrollbar.pack(side="right", fill="y")

#         self.canvas.configure(yscrollcommand=self.scrollbar.set)

#         self.frame_content = tk.Frame(self.canvas)
#         self.canvas.create_window((0, 0), window=self.frame_content, anchor="nw")

#         self.create_content()

#         self.frame_content.bind("<Configure>", self.on_frame_configure)

#         # Botones al final
#         self.botones_frame = tk.Frame(root)
#         self.botones_frame.pack(pady=10)

#         self.cancelar_button = tk.Button(self.botones_frame, text="Cancelar", command=self.cancelar, width=14, bg="#215B6F", fg="white", font=("Arial", 8))
#         self.cancelar_button.pack(side="left", padx=10)

#         self.continuar_button = tk.Button(self.botones_frame, text="Continuar", command=self.mostrar_resumen_view, width=14, bg="#215B6F", fg="white", font=("Arial", 8))
#         self.continuar_button.pack(side="left", padx=10)

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def create_content(self):
#         self.productos = []
#         for i in range(1, int(self.data_manager.get_cantidad_productos()) + 1):
#             frame_product = tk.Frame(self.frame_content, padx=0, pady=10)
#             frame_product.pack(anchor="w", pady=(0, 10), fill="x")

#             label1 = tk.Label(frame_product, text=f"Producto {i}:", anchor="e", font=("Arial", 10, "bold"))
#             label1.grid(row=0, column=0, sticky="w", padx=(15, 5))

#             label2 = tk.Label(frame_product, text="Nombre del producto:", anchor="e")
#             label2.grid(row=1, column=0, sticky="w", padx=(50, 5), pady=(5, 5))

#             entry2 = tk.Entry(frame_product, width=40)
#             entry2.grid(row=1, column=1, padx=(5, 10), pady=(5, 5))
#             entry2.insert(0, "Ingrese nombre")
            
#             label3 = tk.Label(frame_product, text="Series del producto:", anchor="e")
#             label3.grid(row=2, column=0, sticky="w", padx=(50, 5), pady=(5, 5))

#             entry_series = tk.Entry(frame_product, width=40)
#             entry_series.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))
#             entry_series.insert(0, "Ingrese serie")
#             entry_series.config(state="disabled")

#             button_agregar_serie = tk.Button(frame_product, text="Agregar Serie", command=lambda entry=entry_series: self.abrir_agregar_serie_view(entry), width=14, bg="#BB7223", fg="white", font=("Arial", 8))
#             button_agregar_serie.grid(row=3, column=0, padx=(50, 5), pady=(5, 5))

#             button_reestablecer_serie = tk.Button(frame_product, text="Reestablecer Serie", command=lambda entry=entry_series: self.reestablecer_serie(entry), width=14, bg="#215B6F", fg="white", font=("Arial", 8))
#             button_reestablecer_serie.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))

#             self.productos.append((entry2, entry_series))

#     def reestablecer_serie(self, entry_series):
#         entry_series.config(state="normal")
#         entry_series.delete(0, tk.END)
#         entry_series.insert(0, "")
#         entry_series.config(state="disabled")

#     def abrir_agregar_serie_view(self, entry_target):
#         if not self.agregar_serie_view_window or not self.agregar_serie_view_window.winfo_exists():
#             self.agregar_serie_view_window = tk.Toplevel(self.root)
#             agregar_serie_view = AgregarSerieView(self.agregar_serie_view_window, entry_target, self)

#     def cancelar(self):
#         self.root.withdraw()
#         self.controller.mostrar_ingresar_nuevo()
    
#     def mostrar_resumen_view(self):
#         print("Pasando los datos al resumen...")

#         productos_data = []
#         for entry2, entry_series in self.productos:
#             nombre_producto = entry2.get()
#             serie_producto = entry_series.get()
#             productos_data.append((nombre_producto, serie_producto))

#         self.root.withdraw()
#         self.controller.mostrar_resumen_view()
