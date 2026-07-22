from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from EasyMode import EasyMode
from MediumMode import MediumMode
from HardMode import HardMode
from ImpossibleMode import ImpossibleMode
from Toolbar import ToolBar
from PySide6.QtCore import Qt
import styles

class GameModes(ToolBar):
    def __init__ (self):
        super().__init__()
        self.home_action.triggered.connect(self.go_home)
        self.instructions_action.triggered.connect(self.show_instructions)
        self.setWindowTitle("Select Game Mode")
        self.resize(500,300)

        self.setStyleSheet(styles.MAIN_WINDOW_STYLE)
        self.title_label = QLabel("SELECT A DIFFICULTY")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet(styles.PAGE_TITLE_STYLE)

## Select Difficulty buttons 
        Easy_Button = QPushButton("Easy")
        Easy_Button.setStyleSheet(styles.EASY_BUTTON_STYLE)
        self.easymode_window = EasyMode(self)
        Easy_Button.clicked.connect(self.show_easy_mode)

        Med_Button = QPushButton("Medium")
        Med_Button.setStyleSheet(styles.MEDIUM_BUTTON_STYLE)
        self.mediummode_window = MediumMode(self)
        Med_Button.clicked.connect(self.show_medium_mode)

        Hard_Button = QPushButton("Hard")
        Hard_Button.setStyleSheet(styles.HARD_BUTTON_STYLE)
        self.hardmode_window = HardMode(self)
        Hard_Button.clicked.connect(self.show_hard_mode)

        Impossible_Button = QPushButton("Impossible")
        Impossible_Button.setStyleSheet(styles.IMPOSSIBLE_BUTTON_STYLE)
        self.impossible_window = ImpossibleMode(self)
        Impossible_Button.clicked.connect(self.show_impossible_mode)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.title_label)
        layout.addSpacing(15)
        layout.addWidget(Easy_Button)
        layout.addWidget(Med_Button)
        layout.addWidget(Hard_Button)
        layout.addWidget(Impossible_Button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_easy_mode(self):
        self.easymode_window.reset_game()
        self.easymode_window.show()
        self.hide()

    def show_medium_mode(self):
        self.mediummode_window.reset_game()
        self.mediummode_window.show()
        self.hide()

    def show_hard_mode(self):
        self.hardmode_window.reset_game()
        self.hardmode_window.show()
        self.hide()

    def show_impossible_mode(self):
        self.impossible_window.reset_game()
        self.impossible_window.show()
        self.hide()

    def go_home(self):
        from WelcomeWindow import WelcomeWindow

        self.home_window = WelcomeWindow()
        self.home_window.show()
        self.hide()

    def show_instructions(self):
        from Instructions import Instructions

        self.instructions_window = Instructions()
        self.instructions_window.show()
        self.hide()