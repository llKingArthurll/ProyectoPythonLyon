# main.py

from app.controllers.app_controller import AppController

def main():
    app_controller = AppController()
    app_controller.start()

if __name__ == "__main__":
    main()
