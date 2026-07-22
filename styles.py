# styles.py

# -------------------------
# Main application windows
# -------------------------

MAIN_WINDOW_STYLE = """
QMainWindow {
    background-color: #1E3A5F;
}

QWidget {
    color: #F5F5F5;
}
"""


INSTRUCTIONS_WINDOW_STYLE = """
QMainWindow {
    background-color: #182E4A;
}

QWidget {
    color: #F5F5F5;
}
"""


# -------------------------
# Toolbar
# -------------------------

TOOLBAR_STYLE = """
QToolBar {
    background-color: #252525;
    border: none;
    spacing: 8px;
    padding: 4px;
}

QToolButton {
    color: #F5F5F5;
    background-color: transparent;
    border: none;
    border-radius: 5px;
    padding: 7px 12px;
    font-size: 13px;
}

QToolButton:hover {
    background-color: #404040;
}

QToolButton:pressed {
    background-color: #555555;
}
"""


# -------------------------
# Welcome window
# -------------------------

WELCOME_TITLE_STYLE = """
color: #F5F5F5;
font-size: 30px;
font-weight: bold;
"""

WELCOME_SUBTITLE_STYLE = """
color: #D0D0D0;
font-size: 16px;
"""


# -------------------------
# General titles and labels
# -------------------------

PAGE_TITLE_STYLE = """
color: #F5F5F5;
font-size: 26px;
font-weight: bold;
"""

INSTRUCTION_STYLE = """
color: #F5F5F5;
font-size: 17px;
"""

FEEDBACK_STYLE = """
color: #F2C94C;
font-size: 21px;
font-weight: bold;
"""

LIVES_STYLE = """
color: #F5F5F5;
font-size: 16px;
"""

ATTEMPTS_STYLE = """
color: #D0D0D0;
font-size: 14px;
"""

GAME_OVER_STYLE = """
color: #EB5757;
font-size: 30px;
font-weight: bold;
"""

CONGRATULATIONS_STYLE = """
color: #6FCF97;
font-size: 30px;
font-weight: bold;
"""

END_MESSAGE_STYLE = """
color: #F5F5F5;
font-size: 17px;
"""


# -------------------------
# Standard buttons
# -------------------------

BUTTON_STYLE = """
QPushButton {
    background-color: #4B5563;
    color: #F5F5F5;
    border: 1px solid #64748B;
    border-radius: 8px;
    padding: 9px 16px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #64748B;
}

QPushButton:pressed {
    background-color: #374151;
}
"""


# -------------------------
# Difficulty buttons
# -------------------------

EASY_BUTTON_STYLE = """
QPushButton {
    background-color: #6FCF97;
    color: #102A1C;
    border: none;
    border-radius: 8px;
    padding: 11px 18px;
    font-size: 15px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #8DDBAE;
}

QPushButton:pressed {
    background-color: #52B97C;
}
"""


MEDIUM_BUTTON_STYLE = """
QPushButton {
    background-color: #F2C94C;
    color: #332B0B;
    border: none;
    border-radius: 8px;
    padding: 11px 18px;
    font-size: 15px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #F7D96F;
}

QPushButton:pressed {
    background-color: #D9AE2F;
}
"""


HARD_BUTTON_STYLE = """
QPushButton {
    background-color: #EB5757;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 11px 18px;
    font-size: 15px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #F06F6F;
}

QPushButton:pressed {
    background-color: #C94343;
}
"""


IMPOSSIBLE_BUTTON_STYLE = """
QPushButton {
    background-color: #6B46C1;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 11px 18px;
    font-size: 15px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #805AD5;
}

QPushButton:pressed {
    background-color: #553C9A;
}
"""


# -------------------------
# Number input
# -------------------------

LINE_EDIT_STYLE = """
QLineEdit {
    background-color: #2D2D2D;
    color: #F5F5F5;
    border: 2px solid #555555;
    border-radius: 8px;
    padding: 8px;
    font-size: 14px;
}

QLineEdit:focus {
    border: 2px solid #5DADE2;
}

QLineEdit::placeholder {
    color: #9CA3AF;
}
"""
INSTRUCTIONS_WINDOW_STYLE = """
QMainWindow {
    background-color: #182E4A;
}

QWidget {
    color: #F5F5F5;
}
"""

INSTRUCTIONS_TITLE_STYLE = """
color: #F5F5F5;
font-size: 26px;
font-weight: bold;
"""

INSTRUCTIONS_TEXT_STYLE = """
color: #D0D0D0;
font-size: 15px;
line-height: 1.4;
"""

INSTRUCTIONS_BUTTON_STYLE = """
QPushButton {
    background-color: #4B5563;
    color: #F5F5F5;
    border: 1px solid #64748B;
    border-radius: 8px;
    padding: 9px 16px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #64748B;
}

QPushButton:pressed {
    background-color: #374151;
}
"""