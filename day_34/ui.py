from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()

        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,
                           pady=20, bg=THEME_COLOR)

        self.questions_label = Label(
            text=f"Question {self.quiz_brain.question_number} of {len(self.quiz_brain.question_list)}",
            fg="white",
            bg=THEME_COLOR,
            font=("Courier", 15, "normal"),
            anchor="w")
        self.questions_label.grid(row=0, column=0)

        self.score_label = Label(
            text=f"SCORE: {quiz_brain.score}",
            fg="white",
            bg=THEME_COLOR,
            font=("Courier", 15, "normal"),
            anchor="e")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white",
                             highlightthickness=8,
                             highlightbackground="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=250,
                                                     text=self.quiz_brain.next_question(),
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_image, command=lambda: self.check_answer("true"))
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_image, command=lambda: self.check_answer("false"))
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(highlightthickness=8,
                           highlightbackground="white")
        new_question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=new_question)

    def check_answer(self, answer: str):
        result = self.quiz_brain.check_answer(answer)
        if result:
            self.canvas.config(highlightthickness=8,
                               highlightbackground="green")
        else:
            self.canvas.config(highlightthickness=8,
                               highlightbackground="red")

        self.questions_label.config(
            text=f"Question {self.quiz_brain.question_number} of {len(self.quiz_brain.question_list)}")
        self.score_label.config(text=f"SCORE: {self.quiz_brain.score}")
        self.window.after(500, self.get_next_question)
