from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget

def configuracion_window():
    # Configurar flags de la ventana para permitir maximizar y cerrar
    window_flags = (QtCore.Qt.Window
                    | QtCore.Qt.WindowMaximizeButtonHint
                    | QtCore.Qt.WindowCloseButtonHint)
    return window_flags

def configuracion_tamano_pantalla():
    # Obtener las dimensiones de la pantalla
    screen = QDesktopWidget().screenGeometry()
    
    # Ancho y alto de la pantalla
    screen_width = screen.width()
    screen_height = screen.height()
    
    return screen_width, screen_height
