import tkinter as tk
from tkinter import PhotoImage
from miapp.pantalla_opciones import PantallaOpciones
from miapp.config import screen_width, screen_height

class PantallaBienvenida:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bienvenido al Sistema")
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Agrega un Label para el título "Bienvenido al Sistema"
        titulo_label = tk.Label(self.root, text="Bienvenido al Sistema", font=("Helvetica", 25), pady=10)
        titulo_label.pack()

        # Cargar la imagen y obtener su tamaño original
        self.background_image = PhotoImage(file="resources/images/imagen.png")

        # Coloca la imagen debajo del título
        label = tk.Label(self.root, image=self.background_image)
        label.pack()

        # Agregar un botón para continuar
        self.continuar_button = tk.Button(self.root, text="Continuar", command=self.mostrar_opciones)
        self.continuar_button.pack(pady=10)

    def mostrar_bienvenida(self):
        self.root.mainloop()

    def mostrar_opciones(self):
        opciones_window = tk.Toplevel(self.root)
        opciones = PantallaOpciones(opciones_window)
        self.root.withdraw()
