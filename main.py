from miapp.pantalla_bienvenida import PantallaBienvenida
import tkinter as tk

def main():
    root = tk.Tk()
    pantalla_inicio = PantallaBienvenida(root)
    pantalla_inicio.mostrar_bienvenida()

if __name__ == "__main__":
    main()
