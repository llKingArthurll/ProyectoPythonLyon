from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget, QScrollArea, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from app.data.data_manager import DataManager
<<<<<<< HEAD
=======
from app.views.agregar_serie_view import AgregarSerieView
from PIL import Image, ImageTk

>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

class IngresoProductoView(QDialog):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
<<<<<<< HEAD
        self.setWindowTitle("Ingreso de Producto")
        self.setWindowIcon(QIcon("resources/LogoLyon.ico"))
        self.setFixedSize(800, 600)
        self.initUI()

    def set_controller(self, controller):
        self.controller = controller
=======
        self.agregar_serie_view_window = None
        self.root.title("Ingreso de Producto")
        self.root.geometry("615x500")
        self.root.resizable(False, False)
        self.root.iconbitmap("resources/LogoLyon.ico")
        

        self.label = tk.Label(root, text="Ingresa los datos de los productos", font=("Arial", 15, "bold"))
        self.label.pack(pady=20)
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

<<<<<<< HEAD
        title_label = QLabel("Ingresa los datos de los productos")
        title_label.setStyleSheet("font-size: 15pt; font-weight: bold;")
        layout.addWidget(title_label)
=======
        cantidad_label = tk.Label(root, text=f"Cantidad de productos: {cantidad_productos}", font=("Arial", 12, "bold"))
        cantidad_label.pack(pady=10)
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

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

<<<<<<< HEAD
            agregar_button = QPushButton("Agregar")
            agregar_button.setFixedWidth(150)
            agregar_button.clicked.connect(lambda state, entry=serie_entry: self.abrir_agregar_serie(entry))
            botones_layout.addWidget(agregar_button)
            agregar_button.setStyleSheet("""
            QPushButton {
                background-color: #BB7223;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)
=======
            label1 = tk.Label(frame_product, text=f"Producto {i}:", anchor="e", font=("Arial", 10, "bold"))
            label1.grid(row=0, column=0, sticky="w", padx=(50, 5))
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

            reestablecer_button = QPushButton("Reestablecer")
            reestablecer_button.setFixedWidth(150)
            reestablecer_button.clicked.connect(lambda state, entry=serie_entry: self.reestablecer_serie(entry))
            botones_layout.addWidget(reestablecer_button)
            reestablecer_button.setStyleSheet("""
            QPushButton {
                background-color: #215B6F;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)
            # Agregar cada widget de producto al scroll_layout
            scroll_layout.addWidget(producto_widget)

        # Crear botones de cancelar y continuar en la parte inferior
        botones_layout = QHBoxLayout()
        layout.addLayout(botones_layout)

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cancelar)
        botones_layout.addWidget(cancelar_button)
        cancelar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)

<<<<<<< HEAD
        continuar_button = QPushButton("Continuar")
        continuar_button.clicked.connect(self.continuar)
        botones_layout.addWidget(continuar_button)
        continuar_button.setStyleSheet("""
            QPushButton {
                background-color: #FE6E0C;
                color: white;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)
=======
            entry3 = tk.Entry(frame_product, width=40)
            entry3.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))
            entry3.insert(0, "Ingrese descripción")

            label4 = tk.Label(frame_product, text="Series:", anchor="e")
            label4.grid(row=3, column=0, sticky="w", padx=(50, 5), pady=(5, 5))

            entry_series = tk.Entry(frame_product, width=40, state="readonly")
            entry_series.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))
            entry_series.insert(0, "Ingrese series")

            button_agregar_serie = tk.Button(frame_product, text="Agregar", command=lambda i=i, entry_series=entry_series: self.abrir_agregar_serie_view(entry_series), width=10, bg="#BB7223",fg="white", font=("Arial", 8))
            button_agregar_serie.grid(row=2, column=2, padx=(5, 10), pady=(5, 5))

            button_reestablecer_serie = tk.Button(frame_product, text="Reestablecer", command=lambda entry_series=entry_series: self.reestablecer_serie(entry_series), width=10, bg="#215B6F",fg="white", font=("Arial", 8))
            button_reestablecer_serie.grid(row=3, column=2, padx=(5, 10), pady=(5, 5))

            self.entry_series_dict[i] = entry_series
            self.productos.append((entry2, entry3, entry_series))

        self.cancelar_button = tk.Button(self.frame, text="Cancelar", command=self.cancelar, bg="#FE6E0C",fg="white", height=2, width=10, font=("Arial", 9))
        self.cancelar_button.pack(pady=10, padx=80, side="left", anchor="center")

        self.continuar_button = tk.Button(self.frame, text="Continuar", command=self.mostrar_resumen_view,  bg="#FE6E0C",fg="white", height=2, width=10, font=("Arial", 9))
        self.continuar_button.pack(pady=10, padx=80, side="right", anchor="center")

    def reestablecer_serie(self, entry_series):
        entry_series.config(state="normal")
        entry_series.delete(0, tk.END)
        entry_series.insert(0, "")
        entry_series.config(state="readonly")

    def abrir_agregar_serie_view(self, entry_series):
        if not self.agregar_serie_view_window or not self.agregar_serie_view_window.winfo_exists():
            self.agregar_serie_view_window = tk.Toplevel(self.root)
            agregar_serie_view = AgregarSerieView(self.agregar_serie_view_window, entry_series, self)
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3

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
