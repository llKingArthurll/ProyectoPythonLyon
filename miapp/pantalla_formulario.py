import tkinter as tk
import os
from tkinter import filedialog, messagebox
from datetime import datetime
from tkcalendar import DateEntry
from miapp.config import screen_width, screen_height
from miapp.pantalla_agregar_productos import PantallaAgregarProductos

class PantallaFormulario:
    def __init__(self, root, pantalla_opciones):
        self.root = root
        self.pantalla_opciones = pantalla_opciones
        self.root.title("Ingresar Nuevo")
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.iconbitmap("resources/images/LogoLYON.ico")
        
        self.label = tk.Label(self.root, text="REGISTRAR NUEVA GUÍA", font=("Helvetica", 25))
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
        label1.pack(side="left", padx=5,)
        def validate_guia_input(P):
            return len(P) <= 40 and P.isalnum()
        validation_guia = root.register(validate_guia_input)
        self.entry1 = tk.Entry(frame1, validate="key", validatecommand=(validation_guia, "%P"), width=25)
        self.entry1.pack(side="left")
        self.entry1.focus_set()

        label2 = tk.Label(frame2, text="Nombre de la empresa:", width=20, anchor="e")
        label2.pack(side="left", padx=5)
        def validate_empresa_input(P):
            return len(P) <= 50
        validation_empresa = root.register(validate_empresa_input)
        self.entry2 = tk.Entry(frame2, validate="key", validatecommand=(validation_empresa, "%P"), width=25)
        self.entry2.pack(side="left")

        label4 = tk.Label(frame3, text="Fecha:", width=20, anchor="e")
        label4.pack(side="left", padx=5)
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        self.fecha_var = tk.StringVar(value=fecha_actual)
        self.date_picker = DateEntry(frame3, textvariable=self.fecha_var, date_pattern="dd/mm/yyyy")
        self.date_picker.pack(side="left")
        self.date_picker.bind("<<DateEntrySelected>>", self.date_changed)

        label5 = tk.Label(frame4, text="Cantidad de productos:", width=20, anchor="e")
        label5.pack(side="left", padx=5)
        def validate_cantidad_productos_input(P):
            return len(P) <= 2 and P.isdigit()
        validation_cantidad = root.register(validate_cantidad_productos_input)
        self.entry4 = tk.Entry(frame4, validate="key", validatecommand=(validation_cantidad, "%P"), width=25)
        self.entry4.pack(side="left")

        label6 = tk.Label(frame5, text="Subir guía:", width=20, anchor="e")
        label6.pack(side="left", padx=5)
        upload_button = tk.Button(frame5, text="Subir archivo", command=self.upload_file, bg="#353D87", fg="white" )
        upload_button.pack(side="left")

        self.file_name = tk.StringVar()
        self.file_label = tk.Label(frame5, textvariable=self.file_name, wraplength=200)
        self.file_label.pack(side="left", pady=(5, 0))

        label7 = tk.Label(frame6, text="Subir factura:", width=20, anchor="e")
        label7.pack(side="left", padx=5)
        upload_button2 = tk.Button(frame6, text="Subir archivo", command=self.upload_file2, bg="#353D87", fg="white")
        upload_button2.pack(side="left")

        self.file_name2 = tk.StringVar()
        self.file_label2 = tk.Label(frame6, textvariable=self.file_name2, wraplength=200)
        self.file_label2.pack(side="left", pady=(5, 0))

        frame1.grid(row=0, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame2.grid(row=0, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame3.grid(row=0, column=2, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame4.grid(row=1, column=0, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame5.grid(row=1, column=1, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")
        frame6.grid(row=1, column=2, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")

        # Nuevas filas para mostrar nombres de archivos
        self.file_label_guia = tk.Label(container, text="", wraplength=200)
        self.file_label_guia.grid(row=2, column=0, columnspan=2, pady=(5, 0))
        
        self.file_label_factura = tk.Label(container, text="", wraplength=200)
        self.file_label_factura.grid(row=2, column=1, columnspan=2, pady=(5, 0))

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", padx=10, pady=(10, 100))
        cancel_button = tk.Button(button_frame, text="Cancelar", command=self.cancel, bg="#FE6E0C", fg="white", bd=1, height=3, width=20)
        cancel_button.pack(side="left", padx=50)
        continue_button = tk.Button(button_frame, text="Continuar", command=self.continue_form, bg="#FE6E0C", fg="white", bd=1, height=3, width=20)
        continue_button.pack(side="right", padx=50)

    def date_changed(self, event):
        date = self.date_picker.get_date()
        fecha_formato_deseado = date.strftime("%d/%m/%Y")
        self.fecha_var.set(fecha_formato_deseado)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path:
            if file_path.lower().endswith(".pdf"):
                file_name = os.path.basename(file_path)
                self.file_name.set(f"Nombre de la guía: {file_name}")
                self.file_label_guia.config(text=f"Nombre de la guía: {file_name}")

    def upload_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path:
            if file_path.lower().endswith(".pdf"):
                file_name = os.path.basename(file_path)
                self.file_name2.set(f"Nombre de la factura: {file_name}")
                self.file_label_factura.config(text=f"Nombre de la factura: {file_name}")

    def cancel(self):
        self.root.destroy()
        self.pantalla_opciones.root.deiconify()

    def continue_form(self):
        numero_guia = self.entry1.get()
        nombre_empresa = self.entry2.get()
        cantidad_productos = self.entry4.get().strip()
        fecha = self.fecha_var.get()
        
        # Verificar que se hayan subido los dos archivos
        if not (self.file_name.get() and self.file_name2.get()):
            messagebox.showerror("Error", "Por favor, suba tanto la guía como la factura.")
        elif not (numero_guia and nombre_empresa and cantidad_productos and fecha):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
        elif cantidad_productos.isnumeric() and int(cantidad_productos) > 0:
            self.root.withdraw()  # Oculta la ventana actual
            agregar_productos_window = tk.Toplevel(self.root)
            agregar_productos_screen = PantallaAgregarProductos(agregar_productos_window, numero_guia, nombre_empresa, fecha, cantidad_productos, self.file_name.get(), self.file_name2.get(), self)
        else:
            messagebox.showerror("Error", "Por favor, ingrese una cantidad de productos válida (mayor a 0).")

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaFormulario(root)
    root.mainloop()
