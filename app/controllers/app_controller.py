# app/controllers/app_controller.py
import tkinter as tk
from app.views.bienvenida_view import BienvenidaView
from app.views.opciones_view import OpcionesView
from app.views.ingresar_nuevo_view import IngresarNuevoView
from app.views.ingreso_producto_view import IngresoProductoView
from app.views.buscar_producto_view import BuscarProductoView
from app.views.resumen_productos_view import ResumenProductosView

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.bienvenida_view = BienvenidaView(self.root, self)

    def start(self):
        self.bienvenida_view.mostrar_bienvenida()

    def mostrar_opciones(self):
        self.root.withdraw()
        opciones_root = tk.Toplevel(self.root)
        opciones_view = OpcionesView(opciones_root, self)
        opciones_view.mostrar_opciones()

    def mostrar_ingresar_nuevo(self):
        self.root.withdraw()
        ingresar_nuevo_root = tk.Toplevel(self.root)
        ingresar_nuevo_view = IngresarNuevoView(ingresar_nuevo_root, self)
        ingresar_nuevo_view.mostrar_ingresar_nuevo()

    def mostrar_ingreso_producto(self):
        self.root.withdraw()
        ingreso_producto_root = tk.Toplevel(self.root)
        ingreso_producto_view = IngresoProductoView(ingreso_producto_root, self)
        ingreso_producto_view.mostrar_ingreso_producto()
    
    def mostrar_buscar_producto(self):
        self.root.withdraw()
        buscar_producto_root = tk.Toplevel(self.root)
        buscar_producto_view = BuscarProductoView(buscar_producto_root, self)
        buscar_producto_view.mostrar_buscar_producto()
    
    def mostrar_resumen_view(self):
        self.root.withdraw()
        resumen_productos_root = tk.Toplevel(self.root)
        resumen_view = ResumenProductosView(resumen_productos_root, self)
        resumen_view.mostrar_resumen_view()

if __name__ == "__main__":
    app_controller = AppController()
    app_controller.start()
