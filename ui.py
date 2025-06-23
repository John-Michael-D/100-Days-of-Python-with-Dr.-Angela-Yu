from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=400, height=475)
        self.window.maxsize(width=400, height=475)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.place(x=32, y=25)

        self.questionText = self.canvas.create_text(150, 125, width=280, text="Welcome!", fill="black",
        font=("Arial", 20, "italic"))

        checkImg = PhotoImage(file="./images/true.png")
        self.checkButton = Button(image=checkImg, highlightthickness=0, command=self.userAnswerTrue)
        self.checkButton.place(x=35,y=300)

        crossImg = PhotoImage(file="./images/false.png")
        self.crossButton = Button(image=crossImg, highlightthickness=0, command=self.userAnswerFalse)
        self.crossButton.place(x=225, y=300)

        self.score = 0
        self.scoreText = Label(text=f"Score: {self.score} correct out of {len(self.quiz.question_list)} total questions",
        bg=THEME_COLOR, fg="white", font=("Arial", 14))
        self.scoreText.place(x=15,y=420)

        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        if self.quiz.still_has_questions():
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=qText)
        else:
            self.canvas.itemconfig(self.questionText, text="Congratulations! You've reached the end of the quiz.")
            self.checkButton.config(state="disabled")
            self.crossButton.config(state="disabled")

    def userAnswerTrue(self):
        isRight = self.quiz.check_answer("True")
        self.giveFeedback(isRight)

    def userAnswerFalse(self):
        isRight = self.quiz.check_answer("False")
        self.giveFeedback(isRight)

    def canvasWhite(self):
        self.canvas.configure(bg="white")
        self.getNextQuestion()

    def giveFeedback(self, isRight):
        if isRight:
            self.canvas.configure(bg="green")
            self.score += 1
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.canvasWhite)
        self.scoreText.config(text=f"Score: {self.score} correct out of {len(self.quiz.question_list)} total questions")