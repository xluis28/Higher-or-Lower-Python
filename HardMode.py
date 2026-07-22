from PySide6.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from RandomLogicalHard import RandomHard
from Toolbar import ToolBar
from PySide6.QtCore import Qt
import styles

class HardMode(ToolBar):
    def __init__ (self, gamemodes_windows):
        super().__init__()
        self.home_action.triggered.connect(self.go_home)
        self.instructions_action.triggered.connect(self.show_instructions)
        self.game_over = False
        self.setWindowTitle("Hard Mode")
        self.resize(500,300)
        self.game = RandomHard()
        self.gamemodes_windows = gamemodes_windows
        self.setStyleSheet(styles.MAIN_WINDOW_STYLE)

## Number Picked and lives label and attempts
        self.instructions_label = QLabel("Pick a number between 1 and 1000")
        self.lives_count = QLabel()
        self.update_lives()
        self.attempts = QLabel()
        self.previous_attempt()
## Updates the end label and feedback label
        self.end_label = QLabel("")
        self.end_label.hide()
        self.feedback_label = QLabel("")
        self.feedback_label.hide()

#Game over and Congratulations Labels
        self.game_over_label = QLabel("GAME OVER")
        self.game_over_label.hide()

        self.congratulations_label = QLabel("CONGRATULATIONS")
        self.congratulations_label.hide()

# Text Box and Enter Button
        self.enter_number = QLineEdit()
        self.Enter_Data = QPushButton("Enter")
        self.Enter_Data.clicked.connect(self.button_clicked)

#Set Styling
        self.instructions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions_label.setStyleSheet(styles.INSTRUCTION_STYLE)

        self.feedback_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.feedback_label.setStyleSheet(styles.FEEDBACK_STYLE)

        self.lives_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lives_count.setStyleSheet(styles.LIVES_STYLE)

        self.attempts.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.attempts.setStyleSheet(styles.ATTEMPTS_STYLE)

        self.game_over_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.game_over_label.setStyleSheet(styles.GAME_OVER_STYLE)

        self.congratulations_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.congratulations_label.setStyleSheet(styles.CONGRATULATIONS_STYLE)

        self.end_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.end_label.setStyleSheet(styles.END_MESSAGE_STYLE)

        self.enter_number.setPlaceholderText("Enter you guess")
        self.enter_number.returnPressed.connect(self.button_clicked)
        self.enter_number.setStyleSheet(styles.LINE_EDIT_STYLE)

        self.Enter_Data.setStyleSheet(styles.BUTTON_STYLE)

# Horizontal Layout for Number entered and Enter Button
        Horizontal_layout = QHBoxLayout()
        Horizontal_layout.addWidget(self.enter_number)
        Horizontal_layout.addWidget(self.Enter_Data)


# Vertical layout containing both horizontal layouts
        layout = QVBoxLayout()
        layout.addWidget(self.instructions_label)
        layout.addWidget(self.feedback_label)
        layout.addWidget(self.lives_count)
        layout.addWidget(self.attempts)
        layout.addWidget(self.game_over_label)
        layout.addWidget(self.congratulations_label)
        layout.addWidget(self.end_label)
        layout.addSpacing(15)
        layout.addLayout(Horizontal_layout)
        layout.addStretch()

        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# method to get the results for numbered entered
    def number_entered(self):
        try:
            guess = int(self.enter_number.text())

        except ValueError:
            self.feedback_label.setText(
            "Please enter a valid whole number.")
            self.feedback_label.show()
            self.enter_number.clear()
            self.enter_number.setFocus()
            return
        if guess < 1 or guess > 1000:
            self.feedback_label.setText(
                "Please enter a number between 1 and 1000.")
            self.feedback_label.show()
            self.enter_number.clear()
            self.enter_number.setFocus()
            return
    
        result = self.game.check_guess(guess)
        self.feedback_label.setText(result)
        self.feedback_label.show()
        self.previous_attempt()
        self.update_lives()
        self.update_end_labels()

        self.enter_number.clear()
        self.enter_number.setFocus()

        if self.game.game_over:
            self.game_over = True
            self.Enter_Data.setText("Play Again")
            self.Enter_Data.setAutoDefault(True)

    def button_clicked(self):
        if self.game_over:
            self.restart_game()
        else:
            self.number_entered()

    def restart_game(self):
        self.reset_game()

    def reset_game(self):
        self.game = RandomHard()
        self.game_over = False
        self.enter_number.setDisabled(False)
        self.game_over_label.hide()
        self.congratulations_label.hide()

        self.end_label.clear()
        self.end_label.hide()

        self.instructions_label.show()
        self.instructions_label.setText("Pick a number between 1 and 1000")

        self.feedback_label.clear()
        self.feedback_label.hide()

        self.update_lives()
        self.previous_attempt()

        self.enter_number.clear()
        self.enter_number.show()
        self.Enter_Data.setText("Enter")

    def update_lives(self):
        if not self.game.game_over:
            self.lives_count.setText("Lives: "+ "❤️" * self.game.lives)
        else:
            self.lives_count.clear()

    def previous_attempt(self):
        if len(self.game.previous_attempts) > 0:
            attempts = ", ".join(map(str, self.game.previous_attempts))
            self.attempts.setText("Previous attempts: " + attempts)
        else:
            self.attempts.clear()

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

    def update_end_labels(self):
        if not self.game.game_over:
            self.instructions_label.show()
            self.feedback_label.show()

            self.end_label.hide()
            self.game_over_label.hide()
            self.congratulations_label.hide()
            return
        
        self.instructions_label.hide()
        self.feedback_label.hide()

        self.end_label.setText(f"The secret number was {self.game.secret_number}")
        self.end_label.show()
        self.enter_number.setDisabled(True)


        if self.game.guessed_number:
            self.congratulations_label.show()
            self.game_over_label.hide()
        else:
            self.game_over_label.show()
            self.congratulations_label.hide()