from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QAction
import styles

class ToolBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)

        self.home_action = QAction("Home", self)
        self.instructions_action = QAction("Instructions", self)

        self.toolbar.addAction(self.home_action)
        self.toolbar.addAction(self.instructions_action)
        
        self.toolbar.setStyleSheet(styles.TOOLBAR_STYLE)