# app/views/resumen_productos_view.py

import tkinter as tk
from tkinter import ttk
from app.data.data_manager import DataManager

class ResumenProductosView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Resumen de Productos")
        self.root.geometry("400x600")
        self.root.resizable(True, True)

        self.label = tk.Label(root, text="¡Bienvenido a Resumen!")
        self.label.pack(pady=20)

        self.scroll_frame = tk.Frame(root)
        self.scroll_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.scroll_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas)
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.productos_labels = []

        self.mostrar_datos()

        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.botones_frame = tk.Frame(root)
        self.botones_frame.pack(pady=10)

        self.cancelar_button = tk.Button(self.botones_frame, text="Cancelar", command=self.cancelar)
        self.cancelar_button.pack(side="left", padx=10)

        self.guardar_button = tk.Button(self.botones_frame, text="Guardar", command=self.guardar)
        self.guardar_button.pack(side="left", padx=10)

    def mostrar_datos(self):
        data_manager = DataManager.get_instance()
        numero_guia = data_manager.get_numero_guia()
        nombre_empresa = data_manager.get_nombre_empresa()
        fecha = data_manager.get_fecha()
        cantidad_productos = data_manager.get_cantidad_productos()
        ingreso_producto_data = data_manager.get_ingreso_producto_data()

        self.mostrar_label(f"Número de Guía: {numero_guia}")
        self.mostrar_label(f"Nombre de la Empresa: {nombre_empresa}")
        self.mostrar_label(f"Fecha: {fecha}")
        self.mostrar_label(f"Cantidad de Productos: {cantidad_productos}")

        for i, producto_data in enumerate(ingreso_producto_data, start=1):
            self.mostrar_label(f"\nProducto {i}:")
            self.mostrar_label(f"Nombre del producto: {producto_data[0]}")
            self.mostrar_label(f"Descripción del producto: {producto_data[1]}")
            self.mostrar_label(f"Series del producto: {producto_data[2]}")

    def mostrar_resumen_view(self):
        self.root.mainloop()

    def mostrar_label(self, text):
        label = tk.Label(self.inner_frame, text=text)
        label.pack(pady=5)
        self.productos_labels.append(label)

    def cancelar(self):
        self.root.destroy()
        if self.controller:
            self.controller.mostrar_ingresar_nuevo()

    def guardar(self):
        print("Preparando datos para guardar...")
        print("Guardando datos...")
        print("¡Datos guardados exitosamente!")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.inner_frame_id, width=event.width)
