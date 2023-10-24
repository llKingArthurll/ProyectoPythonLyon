class PantallaDatos:
    def __init__(self, datos):
        self.datos = datos

    def mostrar_datos(self):
        print("Datos ingresados:")
        print(f"Nombre: {self.datos['nombre']}")
        print(f"Edad: {self.datos['edad']}")
