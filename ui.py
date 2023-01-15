from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="question", font=("Ariel", 15, "italic"),
                                                     fill=THEME_COLOR, width=290)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=3, column=1, padx=20, pady=20)
        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=3, column=2, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,text= "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        """Checks answer when user hits true button"""
        if self.quiz.check_user_answer("true"):
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)


    def check_answer_false(self):
        """Checks answer when user hits false button"""
        if self.quiz.check_user_answer("false"):
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
            self.score_label.config(text=f"Score:{self.quiz.score}")

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)