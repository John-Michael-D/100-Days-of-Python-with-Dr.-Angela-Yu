class Brain:

    def __init__(self, qList):
        self.qNumber = 0
        self.qNumberToPrint = 0
        self.qList = qList
        self.score = 0

    def stillHasQuestions(self):
        return self.qNumber < len(self.qList)

    def nextQuestion(self):
        currentQuestion = self.qList[self.qNumber].qText
        self.qNumberToPrint += 1
        givenQuestion = input(f"\nQuestion {self.qNumberToPrint}: {currentQuestion} (True/False)?\n>").strip().lower()
        self.checkAnswer(givenQuestion, self.qList[self.qNumber].qAnswer)
        self.qNumber += 1
        print(f"Your current score is: {self.score} correct out of {self.qNumber} total questions.")

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")