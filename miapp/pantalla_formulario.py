import tkinter as tk
import os

from tkinter import filedialog
from miapp.config import screen_width, screen_height

class PantallaFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingresar Nuevo")
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Obtén la altura de la pantalla
        container = tk.Frame(self.root, padx=250)
        container.pack(expand=True, fill="both")

        frame1 = tk.Frame(container)
        frame2 = tk.Frame(container)
        frame3 = tk.Frame(container)
        frame4 = tk.Frame(container)
        frame5 = tk.Frame(container)

        label1 = tk.Label(frame1, text="Campo 1:")
        label1.pack(side="left", padx=(10, 5))  # Espacio a la izquierda y derecha
        entry1 = tk.Entry(frame1, validate="key", validatecommand=(self.validate_max_length, "%P", 20))
        entry1.pack(side="left")

        label2 = tk.Label(frame2, text="Campo 2:")
        label2.pack(side="left", padx=(10, 5))  # Espacio a la izquierda y derecha
        entry2 = tk.Entry(frame2, validate="key", validatecommand=(self.validate_max_length, "%P", 20))
        entry2.pack(side="left")

        label3 = tk.Label(frame3, text="Campo 3:")
        label3.pack(side="left", padx=(10, 5))  # Espacio a la izquierda y derecha
        entry3 = tk.Entry(frame3, validate="key", validatecommand=(self.validate_max_length, "%P", 20))
        entry3.pack(side="left")

        label4 = tk.Label(frame4, text="Campo 4:")
        label4.pack(side="left", padx=(10, 5))  # Espacio a la izquierda y derecha
        entry4 = tk.Entry(frame4, validate="key", validatecommand=(self.validate_max_length, "%P", 20))
        entry4.pack(side="left")

        label5 = tk.Label(frame5, text="Subir un archivo:")
        label5.pack(side="left", padx=(10, 5))  # Espacio a la izquierda y derecha
        upload_button = tk.Button(frame5, text="Subir archivo", command=self.upload_file)
        upload_button.pack(side="left")

        # StringVar para almacenar el nombre del archivo
        self.file_name = tk.StringVar()

        # Label para mostrar el nombre del archivo seleccionado
        self.file_label = tk.Label(frame5, textvariable=self.file_name, wraplength=200)  # wraplength para envolver el texto si es demasiado largo
        self.file_label.pack(side="left")

        frame1.grid(row=0, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame2.grid(row=0, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame3.grid(row=0, column=2, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame4.grid(row=1, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame5.grid(row=1, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        # Agregar botones "Cancelar" y "Continuar"
        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancelar", command=self.cancel)
        cancel_button.pack(side="left")
        continue_button = tk.Button(button_frame, text="Continuar", command=self.continue_form)
        continue_button.pack(side="right")
        
    def validate_max_length(self, P, max_length):
        if len(P) <= max_length:
            return True
        return False

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path:
            if file_path.lower().endswith(".pdf"):
                # Usamos os.path.basename para obtener solo el nombre del archivo
                file_name = os.path.basename(file_path)
                self.file_name.set(f"Archivo seleccionado: {file_name}")
            else:
                self.file_name.set("Por favor, seleccione un archivo PDF válido.")

    def cancel(self):
        self.root.destroy()  # Cierra la ventana actual (pantalla de formulario)
        self.previous_window.deiconify()  # Vuelve a mostrar la ventana anterior
    
    def continue_form(self):
        # Aquí puedes agregar la lógica para continuar con el formulario
        pass