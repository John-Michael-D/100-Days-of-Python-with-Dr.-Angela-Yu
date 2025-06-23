import requests

responseOpenTrivia = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
responseOpenTrivia.raise_for_status()
responseOpenTriviaData = responseOpenTrivia.json()["results"]

question_data = responseOpenTriviaData