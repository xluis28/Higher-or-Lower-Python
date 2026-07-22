from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QMainWindow
from PySide6.QtCore import Qt
from Instructions import Instructions
from Gameplay import GameModes
import styles

class WelcomeWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Higher or Lower")
        self.resize(500,300)
        self.setStyleSheet(styles.MAIN_WINDOW_STYLE)


        Welcome_Text = QLabel("Welcome to Higher or Lower")
        Welcome_Text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Welcome_Text.setStyleSheet(styles.WELCOME_TITLE_STYLE)

        subtitle_label = QLabel("Can you guess the secret number?")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet(styles.WELCOME_SUBTITLE_STYLE)


        Start_Button = QPushButton("Play")
        Start_Button.setStyleSheet(styles.BUTTON_STYLE)
        Instructions_Button = QPushButton("How to Play")
        Instructions_Button.setStyleSheet(styles.BUTTON_STYLE)

        self.instructions_window = Instructions()
        Instructions_Button.clicked.connect(self.show_instructions)

        self.gamemodes_window = GameModes()
        Start_Button.clicked.connect(self.show_gamemodes)


        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(Welcome_Text)
        layout.addWidget(subtitle_label)
        layout.addSpacing(20)
        layout.addWidget(Start_Button)
        layout.addWidget(Instructions_Button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)

        
    def show_instructions(self):
        self.instructions_window.show()
        self.hide()

    def show_gamemodes(self):
        self.gamemodes_window.show()
        self.hide()

        
