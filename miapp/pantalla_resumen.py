import tkinter as tk

class PantallaResumen:
    def __init__(self, root, cantidad_productos):
        self.root = root
        self.root.title("Resumen")
        
        self.cantidad_productos = cantidad_productos

        # Crear un label para mostrar la cantidad de productos
        label = tk.Label(self.root, text=f"Cantidad de productos: {self.cantidad_productos}")
        label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaResumen(root, 0)
    root.mainloop()
