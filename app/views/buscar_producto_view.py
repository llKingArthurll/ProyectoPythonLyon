# app/views/buscar_producto_view.py
import tkinter as tk

class BuscarProductoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Buscar Producto")

        # Agregar elementos a la ventana según tus necesidades
        label = tk.Label(self.root, text="Ventana de Buscar Producto")
        label.pack(pady=10)

        # Agregar más elementos, botones, entradas, etc., según sea necesario

        # Botón para cerrar la ventana de Buscar Producto y mostrar la de Opciones
        volver_button = tk.Button(self.root, text="Volver a Opciones", command=self.volver_a_opciones)
        volver_button.pack(pady=10)

    def mostrar_buscar_producto(self):
        self.root.mainloop()

    def volver_a_opciones(self):
        # Ocultar la ventana de Buscar Producto
        self.root.withdraw()
        # Mostrar la ventana de Opciones desde el controlador
        self.controller.mostrar_opciones()

# Puedes agregar más lógica y elementos según tus necesidades
if __name__ == "__main__":
    buscar_producto_root = tk.Tk()
    buscar_producto_view = BuscarProductoView(buscar_producto_root, None)  # Pasa el controlador adecuado si es necesario
    buscar_producto_view.mostrar_buscar_producto()
