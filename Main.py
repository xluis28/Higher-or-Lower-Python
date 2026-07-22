from PySide6.QtWidgets import QApplication
from WelcomeWindow import WelcomeWindow
import sys

app = QApplication(sys.argv)
window = WelcomeWindow()
window.show()
app.exec()
