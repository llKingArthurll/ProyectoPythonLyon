# app/views/bienvenida_view.py
import tkinter as tk
from tkinter import PhotoImage
from app.config.screen_config import screen_width, screen_height

class BienvenidaView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("LYON SYSTEM")
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.root.iconbitmap("resources/LogoLyon.ico")

        self.title_label = tk.Label(root, text="Bienvenido(a) al Sistema", font=("Verdana", 25), pady=10, fg="black")
        self.title_label.pack(pady=20)

        imagen_path = "resources/logoFondo.png"
        self.imagen = PhotoImage(file=imagen_path)

        self.imagen_label = tk.Label(root, image=self.imagen)
        self.imagen_label.pack(pady=10)

        self.continuar_button = tk.Button(root, text="Continuar", command=self.continuar_presionado, pady=10,bg="#FE6E0C",fg="white", height=-5, width=10)
        self.continuar_button.pack(pady=10)

    def continuar_presionado(self):
        self.root.withdraw()
        self.controller.mostrar_opciones()

    def mostrar_bienvenida(self):
        self.root.mainloop()
