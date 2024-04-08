import tkinter as tk

class AgregarSerieView:
    def __init__(self, root, entry_target, parent_view):
        self.root = root
        self.entry_target = entry_target
        self.parent_view = parent_view
        self.root.title("Agregar Serie")
        self.root.geometry("350x130")
        self.root.resizable(width=False, height=False)

        label = tk.Label(self.root, text="Agregar Serie:")
        label.pack(pady=10)

        self.entry_serie = tk.Entry(self.root, width=30)
        self.entry_serie.pack(pady=10)
        self.entry_serie.focus_set()

        button_container = tk.Frame(self.root)
        button_container.pack(pady=5)

        button_agregar = tk.Button(button_container, text="Agregar", command=self.agregar_serie, width=10)
        button_agregar.pack(side="left", padx=5)

        button_listo = tk.Button(button_container, text="Listo", command=self.cerrar_ventana, width=10)
        button_listo.pack(side="left", padx=5)

        # Vincular el evento de presionar Enter al método agregar_serie
        self.entry_serie.bind("<Return>", lambda event: self.agregar_serie())

    def agregar_serie(self):
        if not self.root.winfo_exists():
            return
        serie = self.entry_serie.get()

        if serie:
            entry_target_value = self.entry_target.get()
            nueva_serie = f"{entry_target_value}, {serie}" if entry_target_value else serie
            self.entry_target.config(state="normal")
            self.entry_target.delete(0, "end")
            self.entry_target.insert(0, nueva_serie)
            self.entry_target.config(state="disabled")
            self.entry_serie.delete(0, tk.END)
            self.entry_serie.focus_set()

    def cerrar_ventana(self):
        self.root.destroy()
