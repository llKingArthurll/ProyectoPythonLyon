import tkinter as tk
from tkinter import PhotoImage
from miapp.view.pantalla_opciones import PantallaOpciones
from miapp.config import screen_width, screen_height

class PantallaBienvenida:
    def __init__(self, root):
        self.root = root
        self.root.title("LYON SYSTEM")
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.root.iconbitmap("resources/images/LogoLYON.ico")

        titulo_label = tk.Label(self.root, text="Bienvenido(a) al Sistema", font=("Verdana", 25), pady=10, fg="black")
        titulo_label.pack()

        self.background_image = PhotoImage(file="resources/images/logoFondo.png")
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.pack()

        self.continuar_button = tk.Button(self.root, text="CONTINUAR", command=self.mostrar_opciones, bg="#FE6E0C", fg="white", bd=1, height=2, width=15)
        self.continuar_button.pack(pady=10)

    def mostrar_bienvenida(self):
        self.root.mainloop()

    def mostrar_opciones(self):
        self.opciones_window = tk.Toplevel(self.root)
        opciones = PantallaOpciones(self.opciones_window)
        self.root.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaBienvenida(root)
    app.mostrar_bienvenida()
