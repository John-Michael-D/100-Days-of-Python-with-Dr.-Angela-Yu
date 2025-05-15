from QuestionModel import Question
from QuizGameData import questionData
from QuizBrain import Brain

questionBank = []
brain = Brain(questionBank)

for i in range(len(questionData)):
    questionBank.append(Question(questionData[i]["question"], questionData[i]["correct_answer"]))

while brain.stillHasQuestions():
    brain.nextQuestion()

print("\nYou've completed the quiz!")
print(f"Your final score is: {brain.score} correct out of {len(questionBank)}.")