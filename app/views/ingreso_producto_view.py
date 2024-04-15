from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget, QScrollArea, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from app.data.data_manager import DataManager

class IngresoProductoView(QDialog):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Ingreso de Producto")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.setFixedSize(800, 600)
        self.initUI()

    def set_controller(self, controller):
        self.controller = controller

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel("Ingresa los datos de los productos")
        title_label.setStyleSheet("font-size: 15pt; font-weight: bold;")
        layout.addWidget(title_label)

        cantidad_productos = DataManager.get_instance().obtener_cantidad_productos()
        cantidad_productos = int(cantidad_productos)

        # Crear el área de desplazamiento para la lista de productos
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Configura el layout dentro del área de desplazamiento para justificar hacia arriba
        scroll_layout.setAlignment(Qt.AlignTop)
        
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidget(scroll_widget)

        layout.addWidget(scroll_area)

        for i in range(cantidad_productos):
            # Configura cada producto con un layout vertical
            producto_layout = QVBoxLayout()
            producto_widget = QWidget()
            producto_widget.setObjectName(f"producto_widget_{i}")
            producto_widget.setLayout(producto_layout)

            # Agregar etiquetas y campos de entrada para cada producto
            producto_label = QLabel(f"Producto {i + 1}:")
            producto_layout.addWidget(producto_label)

            nombre_label = QLabel("Nombre del producto:")
            nombre_entry = QLineEdit()
            nombre_entry.setObjectName(f"nombre_entry_{i}")
            nombre_entry.setFixedWidth(300)
            producto_layout.addWidget(nombre_label)
            producto_layout.addWidget(nombre_entry)

            serie_label = QLabel("Series del producto:")
            serie_entry = QLineEdit()
            serie_entry.setObjectName(f"serie_entry_{i}")
            serie_entry.setFixedWidth(300)
            serie_entry.setDisabled(True)
            producto_layout.addWidget(serie_label)
            producto_layout.addWidget(serie_entry)

            # Crear botones para agregar y reestablecer serie
            botones_layout = QHBoxLayout()
            producto_layout.addLayout(botones_layout)

            agregar_button = QPushButton("Agregar")
            agregar_button.setFixedWidth(150)
            agregar_button.clicked.connect(lambda state, entry=serie_entry: self.abrir_agregar_serie(entry))
            botones_layout.addWidget(agregar_button)

            reestablecer_button = QPushButton("Reestablecer")
            reestablecer_button.setFixedWidth(150)
            reestablecer_button.clicked.connect(lambda state, entry=serie_entry: self.reestablecer_serie(entry))
            botones_layout.addWidget(reestablecer_button)

            # Agregar cada widget de producto al scroll_layout
            scroll_layout.addWidget(producto_widget)

        # Crear botones de cancelar y continuar en la parte inferior
        botones_layout = QHBoxLayout()
        layout.addLayout(botones_layout)

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cancelar)
        botones_layout.addWidget(cancelar_button)

        continuar_button = QPushButton("Continuar")
        continuar_button.clicked.connect(self.continuar)
        botones_layout.addWidget(continuar_button)

    def cancelar(self):
        self.close()
        self.controller.mostrar_ingresar_nuevo()

    def abrir_agregar_serie(self, entry):
        if self.controller:
            self.controller.mostrar_agregar_serie(entry)

    def reestablecer_serie(self, entry):
        entry.setText("")

    def mostrar_resumen_view(self):
        print("Pasando los datos al resumen...")
        if self.controller:
            self.controller.mostrar_resumen_producto()
        else:
            print("No se puede mostrar el resumen: controlador no especificado.")
        self.close()

    def validar_campos(self):
        cantidad_productos = int(DataManager.get_instance().obtener_cantidad_productos())
             
        for i in range(cantidad_productos):
            producto_widget = self.findChild(QWidget, f"producto_widget_{i}")
            nombre_entry = producto_widget.findChild(QLineEdit, f"nombre_entry_{i}")
            serie_entry = producto_widget.findChild(QLineEdit, f"serie_entry_{i}")
            
            if nombre_entry and serie_entry:
                nombre = nombre_entry.text()
                series = serie_entry.text()
                
                # Verificar si los campos están vacíos
                if nombre.strip() == "" or series.strip() == "":
                    QMessageBox.warning(self, "Campos Vacíos", f"Debes llenar todos los campos para el Producto {i + 1}.")
                    return False  # Detener la función y devolver False si hay campos vacíos
            else:
                print(f"No se encontraron los widgets 'nombre_entry' o 'serie_entry' para el Producto {i + 1}.")

        return True  # Todos los campos están llenos

    def continuar(self):
        if self.validar_campos():
            cantidad_productos = int(DataManager.get_instance().obtener_cantidad_productos())
            
            # Lista para almacenar los productos y sus series
            datos_productos = []

            for i in range(cantidad_productos):
                producto_widget = self.findChild(QWidget, f"producto_widget_{i}")
                nombre_entry = producto_widget.findChild(QLineEdit, f"nombre_entry_{i}")
                serie_entry = producto_widget.findChild(QLineEdit, f"serie_entry_{i}")

                if nombre_entry and serie_entry:
                    nombre = nombre_entry.text()
                    # Convertir la cadena de series en una lista separada por comas
                    series = [s.strip() for s in serie_entry.text().split(',')]
                    
                    # Agregar los datos del producto a datos_productos
                    datos_productos.append({
                        'nombre': nombre,
                        'series': series
                    })

            # Guardar datos_productos en DataManager
            DataManager.get_instance().guardar_datos_productos(datos_productos)

            # Mostrar la vista de resumen
            self.mostrar_resumen_view()
