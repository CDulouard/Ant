from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QVBoxLayout, QScrollArea
from PyQt5.QtCore import QRect
import modules.WindowContent as wc


class MainWindow(QMainWindow):
    map = []

    def __init__(self, map):
        super().__init__()
        self.map = map
        self.setUI()

    def setUI(self):
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(qApp.exit)

        menu = self.menuBar()
        fichierMenu = menu.addMenu("&Fichier")
        fichierMenu.addAction(exitAction)

        # ========

        self.addcontent()

        # =======
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Smart Ant')
        self.statusBar().showMessage('status')
        self.showMaximized()

    def addcontent(self):
        temp = self.map.get_map()
        height = len(temp)
        width = len(temp[0])

        content = wc.WindowContent(self.map)

        layout = QVBoxLayout(content)

        self.scrollArea = QScrollArea(content)

        layout.addWidget(self.scrollArea)

        self.scrollAreaWidgetContents = wc.WindowContent(self.map)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, (width * 20) + 200, (height * 20) + 200))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.setCentralWidget(self.scrollArea)
