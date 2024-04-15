from PyQt5 import QtWidgets, QtGui, QtCore
from app.data.db_queries import DatabaseQueries

class BuscarSerieView(QtWidgets.QWidget):
    def __init__(self, id_nuevo_ingreso):
        super().__init__()

        # Almacenar el ID recibido
        self.id_nuevo_ingreso = id_nuevo_ingreso
        
        # Configurar la ventana
        self.setWindowTitle("Buscar Serie")
        self.setGeometry(100, 100, 600, 600)  # Ajusta la posición y tamaño de la ventana según lo necesites
        self.setWindowIcon(QtGui.QIcon("resources/LogoLyon.ico"))

        # Instanciar el objeto de consultas a la base de datos
        self.db_queries = DatabaseQueries()
        
        # Configuración de la interfaz de usuario
        self.configurar_ui()

    def configurar_ui(self):
        # Crear un diseño vertical para los elementos en la ventana
        layout_principal = QtWidgets.QVBoxLayout()
        # Justificar el diseño hacia arriba y centrarlo horizontalmente
        layout_principal.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        
        # Crear un QLabel para el título
        titulo_label = QtWidgets.QLabel("Buscando serie...")
        titulo_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        titulo_label.setAlignment(QtCore.Qt.AlignCenter)
        layout_principal.addWidget(titulo_label)

        # Obtener el número de guía y el nombre de la empresa según el ID nuevo ingreso
        numero_guia = self.db_queries.obtener_numero_guia_por_id(self.id_nuevo_ingreso)
        nombre_empresa = self.db_queries.obtener_nombre_empresa_por_id(self.id_nuevo_ingreso)

        # Verifica si se han obtenido los datos
        if numero_guia and nombre_empresa:
            # Crear QLabel para mostrar el número de guía
            etiqueta_numero_guia = QtWidgets.QLabel(f"Número de guía: {numero_guia}")
            layout_principal.addWidget(etiqueta_numero_guia)

            # Crear QLabel para mostrar el nombre de la empresa
            etiqueta_nombre_empresa = QtWidgets.QLabel(f"Nombre de la empresa: {nombre_empresa}")
            layout_principal.addWidget(etiqueta_nombre_empresa)

        # Crear una tabla para mostrar los productos y series
        self.tabla = QtWidgets.QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Nombre Producto", "Series"])
        
        # Configurar la tabla para adaptarse al contenido
        self.tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        
        # Configurar el tamaño mínimo y máximo de la tabla
        self.tabla.setMinimumWidth(400)
        self.tabla.setMaximumWidth(800)
        self.tabla.setMinimumHeight(300)
        self.tabla.setMaximumHeight(600)
        
        # Añadir la tabla al diseño principal
        layout_principal.addWidget(self.tabla)

        # Establecer el diseño principal de la ventana
        self.setLayout(layout_principal)

        # Mostrar los datos de la base de datos en la tabla
        self.mostrar_datos_en_tabla()

    def mostrar_datos_en_tabla(self):
        resultados = self.db_queries.obtener_productos_por_id_nuevo_ingreso(self.id_nuevo_ingreso)

        if not resultados:
            print(f"No se encontraron datos para el ID nuevo ingreso: {self.id_nuevo_ingreso}")
            return
        
        self.tabla.setRowCount(len(resultados))
        
        # Insertar los datos en la tabla
        for i, registro in enumerate(resultados):
            nombre_producto = QtWidgets.QTableWidgetItem(str(registro[0]))
            series_producto = QtWidgets.QTableWidgetItem(str(registro[1]))
            
            nombre_producto.setTextAlignment(QtCore.Qt.AlignCenter)
            series_producto.setTextAlignment(QtCore.Qt.AlignCenter)
            
            self.tabla.setItem(i, 0, nombre_producto)
            self.tabla.setItem(i, 1, series_producto)

        # Ajustar la altura de la fila según el contenido
        self.tabla.resizeRowsToContents()

    def set_controller(self, controller):
        self.controller = controller
