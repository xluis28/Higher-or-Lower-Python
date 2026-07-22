import random

class RandomMedium:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.lives = 7
        self.previous_attempts = []
        self.game_over = False
        self.guessed_number = False

    def check_guess(self, guess):
        self.previous_attempts.append(guess)
        if self.lives <= 0:
            self.previous_attempts = []
            self.game_over = True
            return f"The secret number was {self.secret_number}."

        if guess == self.secret_number:
            self.lives = 0
            self.previous_attempts = []
            self.game_over = True
            self.guessed_number = True
            return f"The secret number was {self.secret_number}!"

        self.lives -= 1

        if self.lives == 0:
            self.previous_attempts = []
            self.game_over = True
            return f"The secret number was {self.secret_number}."

        if guess < self.secret_number:
            return f"Too low! Try again"

        else:
            return f"Too high! Try again"