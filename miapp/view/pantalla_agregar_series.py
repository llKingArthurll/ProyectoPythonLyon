import tkinter as tk
from tkinter import ttk

class PantallaAgregarSeries:
    def __init__(self, root, entry_series, pantalla_agregar_productos):
        self.root = root
        self.entry_series = entry_series
        self.pantalla_agregar_productos = pantalla_agregar_productos
        self.root.title("Agregar Series")
        self.root.geometry("400x300")

        self.label_titulo = tk.Label(self.root, text="Ingrese las series:", font=("inter", 14))
        self.label_titulo.pack(pady=(10, 20))

        self.entry_series_var = tk.StringVar()
        self.entry_series_var.trace_add("write", self.limitar_caracteres)
        
        self.entry_series_input = tk.Entry(self.root, textvariable=self.entry_series_var, font=("inter", 12))
        self.entry_series_input.pack(pady=(0, 20), padx=10, ipady=5, fill="both", expand=True)

        self.boton_guardar = tk.Button(self.root, text="Guardar", command=self.guardar_series, bg="#FE6E0C", fg="white", bd=1, height=2, width=15)
        self.boton_guardar.pack(pady=(0, 10))

    def limitar_caracteres(self, *args):
        series_ingresadas = self.entry_series_var.get()
        if len(series_ingresadas) > 200:
            self.entry_series_var.set(series_ingresadas[:200])

    def guardar_series(self):
        series_ingresadas = self.entry_series_var.get()
        self.entry_series.config(state="normal")
        self.entry_series.delete(0, tk.END)
        self.entry_series.insert(0, series_ingresadas)
        self.entry_series.config(state="readonly")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAgregarSeries(root, None, None)
    root.mainloop()
