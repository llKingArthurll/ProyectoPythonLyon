import tkinter as tk
import os

from tkinter import filedialog
from tkcalendar import DateEntry
from miapp.config import screen_width, screen_height
from miapp.pantalla_resumen import PantallaResumen
from miapp.pantalla_agregar_productos import PantallaAgregarProductos

class PantallaFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingresar Nuevo")
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        self.label = tk.Label(self.root, text="Registrar Nueva Guía", font=("Helvetica", 25))
        self.label.pack(pady=25)

        container = tk.Frame(self.root, padx=250)
        container.pack(expand=True, fill="both")
        
        frame1 = tk.Frame(container)
        frame2 = tk.Frame(container)
        frame3 = tk.Frame(container)
        frame4 = tk.Frame(container)
        frame5 = tk.Frame(container)
        frame6 = tk.Frame(container)

        label1 = tk.Label(frame1, text="N° de guía:", width=20, anchor="e")
        label1.pack(side="left", padx=5)
        def validate_guia_input(P):
            return len(P) <= 40 and P.isalnum()
        validation_guia = root.register(validate_guia_input)
        self.entry1 = tk.Entry(frame1, validate="key", validatecommand=(validation_guia, "%P"), width=25)
        self.entry1.pack(side="left")

        label2 = tk.Label(frame2, text="Nombre de la empresa:", width=20, anchor="e")
        label2.pack(side="left", padx=5)
        def validate_empresa_input(P):
            return len(P) <= 50 and P.isalpha()
        validation_empresa = root.register(validate_empresa_input)
        self.entry2 = tk.Entry(frame2, validate="key", validatecommand=(validation_empresa, "%P"), width=25)
        self.entry2.pack(side="left")

        label3 = tk.Label(frame3, text="Fecha:", width=20, anchor="e")
        label3.pack(side="left", padx=5)
        self.fecha_var = tk.StringVar()
        date_picker = DateEntry(frame3, textvariable=self.fecha_var, date_pattern="dd/mm/yyyy")
        date_picker.pack(side="left")

        label4 = tk.Label(frame4, text="Cantidad de productos:", width=20, anchor="e")
        label4.pack(side="left", padx=5)
        def validate_cantidad_productos_input(P):
            return len(P) <= 2 and P.isdigit()
        validation_cantidad = root.register(validate_cantidad_productos_input)
        self.entry4 = tk.Entry(frame4, validate="key", validatecommand=(validation_cantidad, "%P"), width=25)
        self.entry4.pack(side="left")

        label5 = tk.Label(frame5, text="Subir guía:", width=20, anchor="e")
        label5.pack(side="left", padx=5)
        upload_button = tk.Button(frame5, text="Subir archivo", command=self.upload_file)
        upload_button.pack(side="left")

        self.file_name = tk.StringVar()
        self.file_label = tk.Label(frame5, textvariable=self.file_name, wraplength=200)
        self.file_label.pack(side="left")

        label6 = tk.Label(frame6, text="Subir factura:", width=20, anchor="e")
        label6.pack(side="left", padx=5)
        upload_button2 = tk.Button(frame6, text="Subir archivo", command=self.upload_file2)
        upload_button2.pack(side="left")

        self.file_name2 = tk.StringVar()
        self.file_label2 = tk.Label(frame6, textvariable=self.file_name2, wraplength=200)
        self.file_label2.pack(side="left")

        frame1.grid(row=0, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame2.grid(row=0, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame3.grid(row=0, column=2, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame4.grid(row=1, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame5.grid(row=1, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame6.grid(row=1, column=2, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")

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

    def upload_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path:
            if file_path.lower().endswith(".pdf"):
                file_name = os.path.basename(file_path)
                self.file_name2.set(f"Segundo archivo seleccionado: {file_name}")
            else:
                self.file_name2.set("Por favor, seleccione un archivo PDF válido")

    def cancel(self):
        self.root.destroy()
        self.previous_window.deiconify()

    def continue_form(self):
        cantidad_productos = self.entry4.get().strip()
        agregar_productos_window = tk.Toplevel(self.root)
        agregar_productos_screen = PantallaAgregarProductos(agregar_productos_window, cantidad_productos)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaFormulario(root)
    root.mainloop()
