from miapp.pantalla_bienvenida import PantallaBienvenida
import tkinter as tk

class MiApp:
    def __init__(self, root):
        self.root = root
        self.pantalla_inicio = PantallaBienvenida(self.root)

    def run(self):
        self.pantalla_inicio.mostrar_bienvenida()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MiApp(root)
    app.run()
