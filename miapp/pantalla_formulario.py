import tkinter as tk
import os

from tkinter import filedialog
from miapp.config import screen_width, screen_height
from miapp.pantalla_resumen import PantallaResumen

class PantallaFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingresar Nuevo")
        self.root.geometry(f"{screen_width}x{screen_height}")

        container = tk.Frame(self.root, padx=250)
        container.pack(expand=True, fill="both")
        
        frame1 = tk.Frame(container)
        frame2 = tk.Frame(container)
        frame3 = tk.Frame(container)
        frame4 = tk.Frame(container)
        frame5 = tk.Frame(container)

        label1 = tk.Label(frame1, text="Campo 1:")
        label1.pack(side="left", padx=(10, 5))
        entry1 = tk.Entry(frame1)
        entry1.pack(side="left")

        label2 = tk.Label(frame2, text="Campo 2:")
        label2.pack(side="left", padx=(10, 5))
        entry2 = tk.Entry(frame2)
        entry2.pack(side="left")

        label3 = tk.Label(frame3, text="Campo 3:")
        label3.pack(side="left", padx=(10, 5))
        entry3 = tk.Entry(frame3)
        entry3.pack(side="left")

        self.cantidad_productos = tk.StringVar()
        label4 = tk.Label(frame4, text="Cantidad de productos:")
        label4.pack(side="left", padx=(10, 5))
        self.entry4 = tk.Entry(frame4, textvariable=self.cantidad_productos)
        self.entry4.pack(side="left")

        label5 = tk.Label(frame5, text="Subir un archivo:")
        label5.pack(side="left", padx=(10, 5))
        upload_button = tk.Button(frame5, text="Subir archivo", command=self.upload_file)
        upload_button.pack(side="left")

        self.file_name = tk.StringVar()
        self.file_label = tk.Label(frame5, textvariable=self.file_name, wraplength=200)
        self.file_label.pack(side="left")

        frame1.grid(row=0, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame2.grid(row=0, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame3.grid(row=0, column=2, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame4.grid(row=1, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame5.grid(row=1, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", padx=10, pady=(10, 100))
        cancel_button = tk.Button(button_frame, text="Cancelar", command=self.cancel)
        cancel_button.pack(side="left", padx=50)
        continue_button = tk.Button(button_frame, text="Continuar", command=self.continue_form)
        continue_button.pack(side="right", padx=50)
        
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path:
            if file_path.lower().endswith(".pdf"):
                file_name = os.path.basename(file_path)
                self.file_name.set(f"Archivo seleccionado: {file_name}")
            else:
                self.file_name.set("Por favor, seleccione un archivo PDF válido")

    def cancel(self):
        self.root.destroy()
        self.previous_window.deiconify()

    def continue_form(self):
        cantidad_productos = self.entry4.get().strip()
        print(f"Valor ingresado en cantidad_productos (antes de la validación): '{cantidad_productos}'")

        if cantidad_productos and cantidad_productos.isdigit() and int(cantidad_productos) > 0:
            cantidad_productos = int(cantidad_productos)
            if cantidad_productos > 0:
                print(f"Valor ingresado en cantidad_productos: {cantidad_productos}")
                cantidad_productos_window = tk.Toplevel(self.root)
                cantidad_productos_screen = PantallaResumen(cantidad_productos_window, cantidad_productos)  # Usar PantallaResumen
            else:
                print("La cantidad de productos debe ser un número mayor que 0.")
        else:
            print("La cantidad de productos ingresada no es válida.")

    