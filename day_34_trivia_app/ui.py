from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # score label
        self.score_label = Label(text=f"Score: Test", fg='white', background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        # canvas to hold question
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background='white')
        self.question_text = self.canvas.create_text(150, 125, text="Test", 
                            font=('Arial', 20, 'italic'), width = 280, fill='black')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.respond_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.respond_false)
        self.false_button.grid(row=2, column=1)

        # start questions, keep window open
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        '''Displays next question and updates score.'''
        self.canvas.config(background='white')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfigure(self.question_text, text=f"End of quiz.\nFinal score: {self.quiz.score}/10")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def respond_true(self):
        '''Evaluates a response of "true" within the quiz brain object.'''
        self.give_feedback(self.quiz.check_answer("True"))

    def respond_false(self):
        '''Evaluates a response of "false" within the quiz brain object.'''
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        '''Returns boolean from within quiz brain object and flashes quiz UI green or red accordingly,
        then calls next question.'''
        if is_right:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)