from PySide6.QtWidgets import QApplication
from WelcomeWindow import WelcomeWindow
from PySide6.QtGui import QIcon
import sys

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("Images/Arrows Icon.png"))
window = WelcomeWindow()
window.show()
app.exec()
