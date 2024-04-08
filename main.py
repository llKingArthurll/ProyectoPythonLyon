import sys
from PyQt5.QtWidgets import QApplication
from app.controllers.app_controller import AppController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec_())
