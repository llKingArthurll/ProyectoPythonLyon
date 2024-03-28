import tkinter as tk

class AgregarSerieView:
    def __init__(self, root, entry_target, pantalla_agregar_productos):
        self.root = root
        self.entry_target = entry_target
        self.pantalla_agregar_productos = pantalla_agregar_productos
        self.root.title("Agregar Serie")
        self.root.resizable(width=False, height=False)
        self.root.geometry("300x130")

        label = tk.Label(self.root, text="Agregar Serie:")
        label.pack(pady=10)

        self.entry_serie = tk.Entry(self.root, width=30)
        self.entry_serie.pack(pady=10)
        self.entry_serie.focus_set()

        button_listo = tk.Button(self.root, text="Listo", command=self.cerrar_ventana, width=10)
        button_listo.pack(side="bottom", pady=10)

        # Esperar 100 milisegundos antes de iniciar la detección de eventos
        self.root.after(100, self.listen_for_input)

    def listen_for_input(self):
        self.root.after(100, self.listen_for_input)

    def agregar_serie(self):
        if not self.root.winfo_exists():
            return
        serie = self.entry_serie.get()

        if serie:
            entry_target_value = self.entry_target.get()
            nueva_serie = f"{entry_target_value} {serie}" if entry_target_value else serie
            self.entry_target.config(state="normal")
            self.entry_target.delete(0, tk.END)
            self.entry_target.insert(0, nueva_serie)
            self.entry_target.config(state="readonly")
            self.entry_serie.delete(0, tk.END)
            self.entry_serie.focus_set()

    def cerrar_ventana(self):
        self.root.destroy()
