import tkinter as tk
from tkinter import PhotoImage
from miapp.pantalla_opciones import PantallaOpciones
from miapp.config import screen_width, screen_height
from tkinter import ttk

class PantallaBienvenida:
    def __init__(self, root):
        self.root = root
        self.root.title("LYON  SYSTEM")
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Agregar un ícono
        self.root.iconbitmap("resources/images/LogoLYON.ico")
    
        # Agregar un Label para el título "Bienvenido al Sistema" con color anaranjado
        titulo_label = tk.Label(self.root, text="BIENVENIDO AL SISTEMA", font=("Verdana", 25), pady=10, fg="black")
        titulo_label.pack()

        # Cargar la imagen de fondo personalizado
        self.background_image = PhotoImage(file="resources/images/logoFondo.png")  # Reemplaza con la ruta de tu imagen
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.pack()

        # Agregar un botón 
        self.continuar_button = tk.Button(self.root, text="CONTINUAR", command=self.mostrar_opciones, bg="#FE6E0C", fg="white", bd=1, height=2, width=15)
        self.continuar_button.pack(pady=10)

    def mostrar_bienvenida(self):
        self.root.mainloop()

    def mostrar_opciones(self):
        opciones_window = tk.Toplevel(self.root)
        opciones = PantallaOpciones(opciones_window)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaBienvenida(root)
    root.mainloop()