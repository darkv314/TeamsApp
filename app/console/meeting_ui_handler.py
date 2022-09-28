from textwrap import indent
from app.console.meeting_ui_menu import QuizUIMenu
from app.model.quiz import Quiz
from app.utils.filter_response import *

class QuizUIHandler(object):

    @staticmethod
    def create_quiz(option) -> Quiz:
        menu = QuizUIMenu()
        return menu.handle_create_quiz(option)

    @staticmethod
    def show_info(quiz: Quiz):
        DIR_PATH = '/Coding/Jala/Python/teams_app/app/attendance_reports'
        start_date = dt.strptime(quiz.start_date,'%m/%d/%Y')
        end_date = dt.strptime(quiz.end_date,'%m/%d/%Y')
        date_dir = get_dirs(DIR_PATH, start_date, end_date)
        print(create_new_date(date_dir, quiz.title, start_date, end_date, quiz.option))

        
        