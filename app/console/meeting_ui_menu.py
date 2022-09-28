from app.model.quiz import Quiz


class QuizUIMenu(object):
    MENU_PROMPT = "> "

    def ask_question_meeting_title(self):
        return input('Menu title'+self.MENU_PROMPT)

    def ask_question_start_date(self):
        return input('Start date'+self.MENU_PROMPT)

    def ask_question_end_date(self):
        return input('End date'+self.MENU_PROMPT)

    def handle_create_quiz(self, option) -> Quiz:
        title = self.ask_question_meeting_title()
        start_date = self.ask_question_start_date()
        end_date = self.ask_question_end_date()

        quiz = Quiz(title, start_date, end_date, option)
        
        return quiz
        
        