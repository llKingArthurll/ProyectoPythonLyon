import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from tkcalendar import DateEntry
from miapp.config import screen_width, screen_height
from miapp.view.pantalla_agregar_productos import PantallaAgregarProductos

class ValidadorInput:
    @staticmethod
    def validar_alphanumeric(P, max_length):
        return len(P) <= int(max_length) and P.isalnum()

    @staticmethod
    def validar_texto(P, max_length):
        return len(P) <= int(max_length)

    @staticmethod
    def validar_numero(P, max_length):
        return len(P) <= int(max_length) and P.isdigit()

class PantallaFormulario:
    def __init__(self, root, pantalla_opciones):
        self.root = root
        self.pantalla_opciones = pantalla_opciones
        self.configurar_ventana()

        self.label = tk.Label(self.root, text="Registrar Nueva Guía", font=("Helvetica", 25))
        self.label.pack(pady=25)

        container = tk.Frame(self.root, padx=250)
        container.pack(expand=True, fill="both")

        self.crear_frames(container)
        self.crear_botones(container)

    def configurar_ventana(self):
        self.root.title("Ingresar Nuevo")
        self.root.geometry(f"{screen_width}x{screen_height}")

    def crear_frames(self, container):
        self.frames = []
        self.file_name_guia = tk.StringVar()
        self.file_name_factura = tk.StringVar()

        frame1 = self.crear_frame_input(container, "N° de guía:", ValidadorInput.validar_alphanumeric, 40, focus=True)
        frame2 = self.crear_frame_input(container, "Nombre de la empresa:", ValidadorInput.validar_texto, 50)
        frame3 = self.crear_frame_fecha(container)
        frame4 = self.crear_frame_input(container, "Cantidad de productos:", ValidadorInput.validar_numero, 2)
        frame5 = self.crear_frame_archivo(container, "Subir guía:", self.upload_file, self.file_name_guia)
        frame6 = self.crear_frame_archivo(container, "Subir factura:", self.upload_file2, self.file_name_factura)

        self.frames.extend([frame1, frame2, frame3, frame4, frame5, frame6])
        self.posicionar_frames(container)

    def crear_frame_input(self, container, label_text, validation_func, max_length, focus=False):
        frame = tk.Frame(container)
        label = tk.Label(frame, text=label_text, width=20, anchor="e")
        label.pack(side="left", padx=5)

        validation_command = (self.root.register(validation_func), "%P", max_length)
        entry = tk.Entry(frame, validate="key", validatecommand=validation_command, width=25)
        entry.pack(side="left")
        if focus:
            entry.focus_set()

        return frame

    def crear_frame_fecha(self, container):
        frame = tk.Frame(container)
        label = tk.Label(frame, text="Fecha:", width=20, anchor="e")
        label.pack(side="left", padx=5)

        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        fecha_var = tk.StringVar(value=fecha_actual)
        date_picker = DateEntry(frame, textvariable=fecha_var, date_pattern="dd/mm/yyyy")
        date_picker.pack(side="left")
        date_picker.bind("<<DateEntrySelected>>", self.date_changed)

        return frame

    def crear_frame_archivo(self, container, label_text, command_func, file_name_var):
        frame = tk.Frame(container)
        label = tk.Label(frame, text=label_text, width=20, anchor="e")
        label.pack(side="left", padx=5)

        upload_button = tk.Button(frame, text="Subir archivo", command=lambda: command_func(file_name_var))
        upload_button.pack(side="left")

        file_label = tk.Label(frame, textvariable=file_name_var, wraplength=200)
        file_label.pack(side="left", pady=(5, 0))

        return frame

    def posicionar_frames(self, container):
        for i, frame in enumerate(self.frames):
            row, col = divmod(i, 3)
            frame.grid(row=row, column=col, padx=10, pady=(screen_height - 600) // 2, sticky="nsew")

        # Nuevas filas para mostrar nombres de archivos
        self.file_label_guia = tk.Label(container, text="", wraplength=200)
        self.file_label_guia.grid(row=2, column=0, columnspan=2, pady=(5, 0))

        self.file_label_factura = tk.Label(container, text="", wraplength=200)
        self.file_label_factura.grid(row=2, column=1, columnspan=2, pady=(5, 0))

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

    def crear_botones(self, container):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", padx=10, pady=(10, 100))

        cancel_button = tk.Button(button_frame, text="Cancelar", command=self.cancel)
        cancel_button.pack(side="left", padx=50)

        continue_button = tk.Button(button_frame, text="Continuar", command=self.continue_form)
        continue_button.pack(side="right", padx=50)

    def date_changed(self, event):
        date_picker = event.widget
        date = date_picker.get_date()
        fecha_formato_deseado = date.strftime("%d/%m/%Y")
        date_picker.set_date(fecha_formato_deseado)

    def upload_file(self, file_name_var):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path and file_path.lower().endswith(".pdf"):
            file_name = os.path.basename(file_path)
            file_name_var.set(file_name)
            self.file_label_guia.config(text=f"Nombre de la guía: {file_name}")

    def upload_file2(self, file_name_var):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path and file_path.lower().endswith(".pdf"):
            file_name = os.path.basename(file_path)
            file_name_var.set(file_name)
            self.file_label_factura.config(text=f"Nombre de la factura: {file_name}")

    def cancel(self):
        self.root.destroy()
        if self.pantalla_opciones:
            self.pantalla_opciones.root.deiconify()

    def continue_form(self):
        if self.validar_formulario():
            self.mostrar_siguiente_pantalla()

    def validar_formulario(self):
        for frame in self.frames:
            if isinstance(frame.winfo_children()[1], tk.Entry):  # Verificar si es un widget de tipo Entry
                entry = frame.winfo_children()[1]  # Acceder al widget Entry dentro de cada frame
                if not entry.get().strip():
                    messagebox.showerror("Error", "Por favor, complete todos los campos.")
                    return False
        if not (self.file_name_guia.get() and self.file_name_factura.get()):
            messagebox.showerror("Error", "Por favor, suba tanto la guía como la factura.")
            return False
        cantidad_productos = self.frames[3].winfo_children()[1].get().strip()
        if not cantidad_productos.isnumeric() or int(cantidad_productos) <= 0:
            messagebox.showerror("Error", "Por favor, ingrese una cantidad de productos válida (mayor a 0).")
            return False
        return True

    def mostrar_siguiente_pantalla(self):
        self.root.withdraw()
        numero_guia = self.frames[0].winfo_children()[1].get().strip()
        nombre_empresa = self.frames[1].winfo_children()[1].get().strip()
        fecha = self.frames[2].winfo_children()[1].get().strip()
        cantidad_productos = self.frames[3].winfo_children()[1].get().strip()
        file_name_guia = self.file_name_guia.get().strip()
        file_name_factura = self.file_name_factura.get().strip()

        agregar_productos_window = tk.Toplevel(self.root)
        agregar_productos_screen = PantallaAgregarProductos(
            agregar_productos_window,
            numero_guia,
            nombre_empresa,
            fecha,
            cantidad_productos,
            file_name_guia,
            file_name_factura,
            self
        )
        agregar_productos_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaFormulario(root, None)
    root.mainloop()
