import tkinter as tk

class PantallaForms:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingrese nueva guía")

        # Crear un Frame para organizar los elementos en tres columnas
        self.column1 = tk.Frame(self.root)
        self.column1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.column2 = tk.Frame(self.root)
        self.column2.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.column3 = tk.Frame(self.root)
        self.column3.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        # Título
        self.label_title = tk.Label(self.root, text="Ingrese nueva guía", font=("Helvetica", 16))
        self.label_title.grid(row=0, columnspan=3, pady=10)

        # Labels y campos de entrada
        self.create_label_entry(self.column1, "Campo 1:")
        self.create_label_entry(self.column1, "Campo 2:")

        self.create_label_entry(self.column1, "Campo 3:")
        self.create_label_entry(self.column1, "Campo 4:")

        self.create_label_entry(self.column2, "Campo 5:")
        self.create_label_entry(self.column2, "Campo 6:")

    def create_label_entry(self, frame, label_text):
        label = tk.Label(frame, text=label_text)
        entry = tk.Entry(frame)
        label.grid(sticky="w")
        entry.grid(sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaForms(root)
    root.mainloop()
