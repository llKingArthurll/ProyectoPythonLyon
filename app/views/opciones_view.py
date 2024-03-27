# app/views/opciones_view.py
import tkinter as tk
from app.config.screen_config import screen_width, screen_height
from PIL import Image, ImageTk
class OpcionesView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Opciones de la Aplicación")
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.label = tk.Label(root, text="¡Bienvenido a las opciones!", font=("Verdana", 25), pady=10, fg="black")
        self.label.pack(pady=20)
        self.root.iconbitmap("resources/LogoLyon.ico")
        
        # Botón con imagen para buscar producto
        img_buscar_producto = tk.PhotoImage(file="resources/Busqueda.png")
        self.buscar_producto_button = tk.Button(
            root,
            text="BUSCAR PRODUCTO",
            command=self.abrir_buscar_producto,
            image=img_buscar_producto,
            compound="top",  # Colocar imagen encima del texto
            pady=20,
            bg="#FE6E0C",
            fg="white",
            bd=1,
            height=150,
            width=200,
        )
        self.buscar_producto_button.image = img_buscar_producto  # Referencia para evitar que la imagen se recolecte basura
        self.buscar_producto_button.pack(side=tk.LEFT, pady=10, padx=350)

        # Botón con imagen para ingresar nuevo
        img_ingresar_nuevo = tk.PhotoImage(file="resources/IngresoGuia.png")
        self.ingresar_nuevo_button = tk.Button(
            root,
            text="INGRESAR NUEVO",
            command=self.abrir_ingresar_nuevo,
            image=img_ingresar_nuevo,
            compound="top",  # Colocar imagen encima del texto
            pady=20,
            bg="#FE6E0C",
            fg="white",
            bd=1,
            height=150,
            width=200,
        )
        self.ingresar_nuevo_button.image = img_ingresar_nuevo  # Referencia para evitar que la imagen se recolecte basura
        self.ingresar_nuevo_button.pack(side=tk.LEFT, pady=10, padx=10)

    def mostrar_opciones(self):
        self.root.mainloop()

    def abrir_buscar_producto(self):
        self.root.withdraw()
        self.controller.mostrar_buscar_producto()

    def abrir_ingresar_nuevo(self):
        self.root.withdraw()
        self.controller.mostrar_ingresar_nuevo()
