from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class Ui():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_txt = Label(text="Score: 0", background=THEME_COLOR, fg="#FFFFFF")
        self.score_txt.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="#FFFFFF",highlightthickness=0)
        self.q_text = self.canvas.create_text(150,125, width=280, text = "text", fill=THEME_COLOR, font=('Arial', 14, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(50,50))

        self.x_button_png = PhotoImage(file="C:\Python\Projects\Day34\images\\false.png")
        self.x_button = Button(image=self.x_button_png, highlightthickness=1, command=self.false_button)
        self.x_button.grid(row=2, column=1)

        self.v_button_png = PhotoImage(file="C:\Python\Projects\Day34\images\\true.png")
        self.v_button = Button(image=self.v_button_png, highlightthickness=1, command=self.ok_button)
        self.v_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def ok_button(self):
        self.user_answer = "True"
        result = self.quiz.check_answer(user_answer = self.user_answer)
        self.give_feedback(result=result)

    def false_button(self):
        self.user_answer = "False"
        result = self.quiz.check_answer(user_answer = self.user_answer)
        self.give_feedback(result=result)

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="End of Quiz")           
            self.v_button.config(command=self.buttons_off)         
            self.x_button.config(command=self.buttons_off)         

    def give_feedback(self, result):
        if result:
            self.score_txt.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(background="green")            
        else:
            self.canvas.config(background="red")            
        self.window.after(1000, self.get_next_question)

    def buttons_off(self):
        pass
