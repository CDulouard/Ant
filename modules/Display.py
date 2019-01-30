import modules.MainWindow as Mwin
from PyQt5.QtWidgets import QApplication
import sys


def display(args, map):
    monApp = QApplication(args)
    window = Mwin.MainWindow(map)
    sys.exit(monApp.exec_())
