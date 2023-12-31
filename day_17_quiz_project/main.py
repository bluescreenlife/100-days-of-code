from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# fill question bank with data from data.py
question_bank = []
for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nFinal score: {quiz.score}/{quiz.question_number}")