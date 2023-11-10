import tkinter as tk

class PantallaAgregarSerie:
    def __init__(self, root, entry_target, pantalla_agregar_productos):
        self.root = root
        self.entry_target = entry_target
        self.pantalla_agregar_productos = pantalla_agregar_productos
        self.root.title("Agregar Serie")
        self.root.geometry("300x120")

        label = tk.Label(self.root, text="Agregar Serie:")
        label.pack(pady=10)

        self.entry_serie = tk.Entry(self.root, width=30)
        self.entry_serie.pack(pady=10)

        button_agregar = tk.Button(self.root, text="Agregar", command=self.agregar_serie)
        button_agregar.pack()

    def agregar_serie(self):
        serie = self.entry_serie.get()
        if serie:
            self.entry_target.configure(state="normal")
            self.entry_target.delete(0, tk.END)
            self.entry_target.insert(0, serie)
            self.entry_target.configure(state="readonly")
            self.root.destroy()
            self.pantalla_agregar_productos.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAgregarSerie(root, None, None)  # Reemplaza None con los valores adecuados
    root.mainloop()
