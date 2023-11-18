from screeninfo import get_monitors

# Obtén las dimensiones de la pantalla
monitor_info = get_monitors()[0]
screen_width = monitor_info.width
screen_height = monitor_info.height