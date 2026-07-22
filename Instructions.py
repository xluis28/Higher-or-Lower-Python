from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from Gameplay import GameModes
from Toolbar import ToolBar
import styles

class Instructions(ToolBar):
    def __init__ (self):
        super().__init__()
        self.home_action.triggered.connect(self.go_home)
        self.instructions_action.triggered.connect(self.show_instructions)
        self.setWindowTitle("How to Play")
        self.resize(500,300)
        self.setStyleSheet(styles.INSTRUCTIONS_WINDOW_STYLE)

        self.instructions_label = QLabel('''
🎯 Goal
Guess the secret number before
you run out of lives.

💡 Hint
The game will tell you if your guess 
is too high or too low.

❤️ Lives
Run out of lives and you lose.

🟢 Easy
Range: 1 - 50
Lives: 6

🟡 Medium
Range: 1 - 100
Lives: 7

🔴 Hard
Range: 1 - 1000
Lives: 8

⚫ Impossible
Range: 1 - 1000
Lives: 8
NO HINTS 💡

Good luck and have fun!
                                   ''')
        self.instructions_label.setStyleSheet(styles.INSTRUCTIONS_TEXT_STYLE)
        self.instructions_label.setWordWrap(True)
        self.instructions_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        Start_Button = QPushButton("Play")
        Start_Button.setStyleSheet(styles.BUTTON_STYLE)

        self.gamemodes_window = GameModes()
        Start_Button.clicked.connect(self.show_gamemodes)


        layout = QVBoxLayout()
        layout.addWidget(self.instructions_label)
        layout.addSpacing(20)
        layout.addStretch()
        layout.addWidget(Start_Button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_gamemodes(self):
        self.gamemodes_window.show()
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