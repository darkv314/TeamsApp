from app.console.meeting_ui_handler import *


class Menu(object):
    MENU_PROMPT ="> "

    def __init__(self):
        # self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Teams Attendance App
===============================
1. Number of participants attending meetings
2. Duration of meetings
3. Exit
        """)

    def process(self):
        self.show_main_menu()
        option = int(input(self.MENU_PROMPT))
        should_exit = False
        if option != 3:
            self.quiz = QuizUIHandler.create_quiz(option)
            QuizUIHandler.show_info(self.quiz)
        else:
            should_exit = True

        return should_exit
