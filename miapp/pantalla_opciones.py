import tkinter as tk
from tkinter import Toplevel

from miapp.config import screen_width, screen_height
from miapp.pantalla_forms import PantallaForms
from miapp.pantalla_formulario import PantallaFormulario

class PantallaOpciones:
    def __init__(self, root):
        self.root = root
        self.root.title("Opciones")
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.label = tk.Label(self.root, text="¿Qué acción deseas reazliar?", font=("Helvetica", 25))
        self.label.pack(pady=25)
        
        self.label = tk.Label(self.root, text="Elige una opción:")
        self.label.pack(pady=20)

        self.ver_archivos_button = tk.Button(self.root, text="Ver archivos", command=self.ver_archivos)
        self.ver_archivos_button.pack(pady=10)

        self.ingresar_nuevo_button = tk.Button(self.root, text="Ingresar nuevo", command=self.ingresar_nuevo)
        self.ingresar_nuevo_button.pack(pady=10)
        
        self.continuar_button = tk.Button(self.root, text="Continuar", command=self.continuar)
        self.continuar_button.pack(pady=10)

    def ver_archivos(self):
        # Agregar lógica para ver archivos o navegar a la pantalla correspondiente aquí
        pass
    
    def ingresar_nuevo(self):
        self.root.withdraw()
        formulario_window = tk.Tk()
        pantalla_formulario = PantallaFormulario(formulario_window)
        pantalla_formulario.previous_window = self.root
        formulario_window.mainloop()
        
    def continuar(self):
        self.root.withdraw()
        formulario_window = tk.Tk()
        pantalla_formulario = PantallaForms(formulario_window)
        pantalla_formulario.previous_window = self.root
        formulario_window.mainloop()
