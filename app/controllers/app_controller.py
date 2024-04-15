from app.views.bienvenida_view import BienvenidaView
from app.views.opciones_view import OpcionesView
from app.views.ingresar_nuevo_view import IngresarNuevoView
from app.views.ingreso_producto_view import IngresoProductoView
from app.views.agregar_serie_view import AgregarSerieView
from app.views.resumen_productos_view import ResumenProductoView
from app.views.buscar_producto_view import BuscarProductoView
from app.views.buscar_serie_view import BuscarSerieView

class AppController:
    def __init__(self):
        self.bienvenida_view = None
        self.opciones_view = None
        self.ingresar_nuevo_view = None
        self.ingreso_producto_view = None
        self.agregar_serie_view = None
        self.resumen_producto_view = None
        self.buscar_producto_view = None
        self.buscar_serie_view = None
        self.show_bienvenida()

    def show_bienvenida(self):
        self.bienvenida_view = BienvenidaView()
        self.bienvenida_view.set_controller(self)
        self.bienvenida_view.show()

    def mostrar_opciones(self):
        if self.opciones_view:
            self.opciones_view.close()
        self.opciones_view = OpcionesView()
        self.opciones_view.set_controller(self)
        self.bienvenida_view.close()
        self.opciones_view.show()

    def mostrar_ingresar_nuevo(self):
        if self.opciones_view:
            self.opciones_view.close()
        self.ingresar_nuevo_view = IngresarNuevoView()
        self.ingresar_nuevo_view.set_controller(self)
        self.ingresar_nuevo_view.exec_()

    def mostrar_ingreso_producto(self):
        if self.ingreso_producto_view:
            self.ingreso_producto_view.close()
        self.ingreso_producto_view = IngresoProductoView(self)
        self.ingreso_producto_view.show()

    def mostrar_agregar_serie(self, entry):
        if self.agregar_serie_view:
            self.agregar_serie_view.close()
        self.agregar_serie_view = AgregarSerieView(entry_target=entry, parent_view=self.ingreso_producto_view)
        self.agregar_serie_view.exec_()
    
    def mostrar_resumen_producto(self):
        if self.resumen_producto_view:
            self.resumen_producto_view.close()
        self.resumen_producto_view = ResumenProductoView()
        self.resumen_producto_view.set_controller(self)
        self.resumen_producto_view.show()

    def mostrar_buscar_producto(self):
        if self.buscar_producto_view:
            self.buscar_producto_view.close()
        self.buscar_producto_view = BuscarProductoView()
        self.buscar_producto_view.set_controller(self)
        self.buscar_producto_view.show()

    def mostrar_buscar_serie(self, id_nuevo_ingreso):
        # Cerrar cualquier instancia existente de BuscarSerieView antes de crear una nueva
        if hasattr(self, 'buscar_serie_view') and self.buscar_serie_view is not None:
            self.buscar_serie_view.close()
            
        # Crear una nueva instancia de BuscarSerieView con el ID de nuevo ingreso
        self.buscar_serie_view = BuscarSerieView(id_nuevo_ingreso)
        self.buscar_serie_view.show()

    
    