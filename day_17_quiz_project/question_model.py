from data import question_data

class Question:
    # creates question objects containing a text (the question) and answer value
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer