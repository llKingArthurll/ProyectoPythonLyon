import tkinter as tk
from miapp.config import screen_width, screen_height
from miapp.view.pantalla_formulario import PantallaFormulario

class PantallaOpciones:
    def __init__(self, root):
        self.root = root
        self.configurar_ventana()

        self.label_bienvenida = tk.Label(self.root, text="¿QUÉ ACCIÓN DESEA REALIZAR?", font=("inter", 25))
        self.label_bienvenida.pack(pady=25)

        self.label_opciones = tk.Label(self.root, text="Elige una opción:")
        self.label_opciones.pack(pady=20)

        self.crear_botones()

    def configurar_ventana(self):
        self.root.title("LYON SYSTEM")
        self.root.geometry(f"{screen_width}x{screen_height}")

    def crear_botones(self):
        self.crear_boton("Busca tu archivo:", self.ver_archivos, relx=0.35, rely=0.40)
        self.crear_boton("Ingresar una nueva Guía:", self.ingresar_nuevo, relx=0.6, rely=0.40)

    def crear_boton(self, text, command, relx, rely):
        label = tk.Label(self.root, text=text)
        label.place(relx=relx, rely=rely)

        button = tk.Button(self.root, text=f"{text.split()[0]}", command=command, bg="#FE6E0C", fg="white", bd=1, height=3, width=20)
        button.place(relx=relx, rely=rely + 0.05)

    def ver_archivos(self):
        pass

    def ingresar_nuevo(self):
        self.root.withdraw()
        formulario_window = tk.Toplevel(self.root)
        pantalla_formulario = PantallaFormulario(formulario_window, self)
        formulario_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaOpciones(root)
    root.mainloop()
