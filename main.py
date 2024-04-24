import sys
import os
from PyQt5.QtWidgets import QApplication
from app.controllers.app_controller import AppController

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec_())
