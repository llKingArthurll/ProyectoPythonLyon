import tkinter as tk
from tkinter import Toplevel
from tkinter import PhotoImage
from miapp.config import screen_width, screen_height
from miapp.pantalla_formulario import PantallaFormulario

import tkinter as tk
class PantallaOpciones:
    def __init__(self, root):
        self.root = root
        self.root.title("LYON  SYSTEM")
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.iconbitmap("resources/images/LogoLYON.ico")
        

        self.label = tk.Label(self.root, text="¿QUÉ ACCIÓN DESEA REALIZAR?", font=("inter", 25))
        self.label.pack(pady=25)
        
        self.label = tk.Label(self.root, text="Elige una opción:")
        self.label.pack(pady=20)

        self.label = tk.Label(self.root, text="Busca tu archivo:")
        self.label.place(relx=0.35, rely=0.35)
        self.ver_archivos_button = tk.Button(self.root, text="Ver archivos", command=self.ver_archivos, bg="#FE6E0C", fg="white", bd=1, height=3, width=20)
        self.ver_archivos_button.place(relx=0.35, rely=0.40)

        self.label = tk.Label(self.root, text="Ingresar una nueva Guía:")
        self.label.place(relx=0.6, rely=0.35)
        self.ingresar_nuevo_button = tk.Button(self.root, text="Ingresar nuevo", command=self.ingresar_nuevo, bg="#FE6E0C", fg="white", bd=1, height=3, width=20)
        self.ingresar_nuevo_button.place(relx=0.6, rely=0.40)

    def ver_archivos(self):
        # Agregar lógica para ver archivos o navegar a la pantalla correspondiente aquí
        pass
    
    def ingresar_nuevo(self):
        self.root.withdraw()
        formulario_window = tk.Tk()
        pantalla_formulario = PantallaFormulario(formulario_window, self)
        formulario_window.mainloop()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaOpciones(root)
    root.mainloop()