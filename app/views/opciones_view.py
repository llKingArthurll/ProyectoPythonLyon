# app/views/opciones_view.py
import tkinter as tk
from app.config.screen_config import screen_width, screen_height

class OpcionesView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Opciones de la Aplicación")
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.label = tk.Label(root, text="¡Bienvenido a las opciones!")
        self.label.pack(pady=20)
        self.buscar_producto_button = tk.Button(root, text="Buscar Producto", command=self.abrir_buscar_producto)
        self.buscar_producto_button.pack(pady=10)
        self.ingresar_nuevo_button = tk.Button(root, text="Ingresar Nuevo", command=self.abrir_ingresar_nuevo)
        self.ingresar_nuevo_button.pack(pady=10)

    def mostrar_opciones(self):
        self.root.mainloop()

    def abrir_buscar_producto(self):
        self.root.withdraw()
        self.controller.mostrar_buscar_producto()

    def abrir_ingresar_nuevo(self):
        self.root.withdraw()
        self.controller.mostrar_ingresar_nuevo()
