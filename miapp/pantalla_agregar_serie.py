import tkinter as tk
import keyboard

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
        self.entry_serie.focus_set()

        button_agregar = tk.Button(self.root, text="Agregar", command=self.agregar_serie, width=10)
        button_agregar.pack(side="left", padx=5)

        button_listo = tk.Button(self.root, text="Listo", command=self.cerrar_ventana, width=10)
        button_listo.pack(side="right", padx=5)

        keyboard.hook(self.handle_key_event)

    def handle_key_event(self, e):
        if e.event_type == keyboard.KEY_DOWN and e.name == "enter":
            self.agregar_serie()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAgregarSerie(root, None, None)
    root.mainloop()
