import tkinter as tk

class PantallaForms:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingresar Nuevo")

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        label = tk.Label(frame, text="Ingresa un valor:")
        label.grid(row=0, column=0, padx=10, pady=5)

        self.valor = tk.StringVar()
        self.entry = tk.Entry(frame, textvariable=self.valor)
        self.entry.grid(row=0, column=1, padx=10, pady=5)

        cancel_button = tk.Button(frame, text="Cancelar", command=self.cancel)
        cancel_button.grid(row=1, column=0, padx=10, pady=5)

        continue_button = tk.Button(frame, text="Continuar", command=self.continue_form)
        continue_button.grid(row=1, column=1, padx=10, pady=5)

    def cancel(self):
        self.root.destroy()

    def continue_form(self):
        valor_ingresado = self.entry.get()
        print(f"Valor ingresado en continue_form: {valor_ingresado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaForms(root)
    root.mainloop()
