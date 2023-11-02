import tkinter as tk

from miapp.config import screen_width, screen_height

class PantallaResumen:
    def __init__(self, root):
        self.root = root
        self.root.title("Resumen")
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.label = tk.Label(self.root, text="Resumen de la Guía", font=("Helvetica", 25))
        self.label.grid(row=0, column=1, pady=20)

        # Crear tres Frames para organizar elementos en tres columnas
        self.column1 = tk.Frame(self.root)
        self.column1.grid(row=1, column=0, padx=10, sticky="w")
        self.column2 = tk.Frame(self.root)
        self.column2.grid(row=1, column=1, padx=10, sticky="w")
        self.column3 = tk.Frame(self.root)
        self.column3.grid(row=1, column=2, padx=10, sticky="w")

        self.label_guia = tk.Label(self.column1, text="N° de guía: ", font=("Helvetica", 12))
        self.label_guia.pack(anchor="w")

        self.label_empresa = tk.Label(self.column1, text="Nombre de la empresa: ", font=("Helvetica", 12))
        self.label_empresa.pack(anchor="w")

        self.label_fecha = tk.Label(self.column1, text="Fecha: ", font=("Helvetica", 12))
        self.label_fecha.pack(anchor="w")

        self.label_cantidad_productos = tk.Label(self.column2, text="Cantidad de productos: ", font=("Helvetica", 12))
        self.label_cantidad_productos.pack(anchor="w")

        self.label_file1 = tk.Label(self.column2, text="Primer archivo: ", font=("Helvetica", 12))
        self.label_file1.pack(anchor="w")

        self.label_file2 = tk.Label(self.column3, text="Segundo archivo: ", font=("Helvetica", 12))
        self.label_file2.pack(anchor="w")

    def show_data(self, guia, empresa, fecha_var, cantidad_productos, file1, file2):
        self.label_guia.config(text=f"N° de guía: {guia}")
        self.label_empresa.config(text=f"Nombre de la empresa: {empresa}")
        fecha = fecha_var.get_date().strftime('%d/%m/%Y')
        self.label_fecha.config(text=f"Fecha: {fecha}")
        self.label_cantidad_productos.config(text=f"Cantidad de productos: {cantidad_productos}")
        self.label_file1.config(text=f"Primer archivo: {file1}")
        self.label_file2.config(text=f"Segundo archivo: {file2}")

        # Crear un Frame adicional para los labels y entrys de la cantidad de productos
        products_frame = tk.Frame(self.root)
        products_frame.grid(row=2, column=1)

        # Crea los labels y entrys
        labels_entries = self.create_labels_entries(cantidad_productos, products_frame)
        for i, (label, entry) in enumerate(labels_entries):
            label.pack(anchor="w")
            entry.pack(anchor="w")

    def create_labels_entries(self, cantidad_productos, frame):
        cantidad_productos = int(cantidad_productos)
        labels_entries = []

        # Especificar el número de columnas y el espacio entre ellas
        frame.grid_columnconfigure(0, weight=1, minsize=100)
        frame.grid_columnconfigure(1, weight=1, minsize=100)
        for i in range(cantidad_productos):
            label = tk.Label(frame, text=f"Producto {i + 1}: ", font=("Helvetica", 12))
            entry = tk.Entry(frame)
            labels_entries.append((label, entry))
        # Ordenar los labels y entrys de izquierda a derecha
        for i in range(min(3, cantidad_productos)):
            label, entry = labels_entries.pop(0)
            label.pack(anchor="w")
            entry.pack(anchor="w")
        return labels_entries

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaResumen(root)
    root.mainloop()
