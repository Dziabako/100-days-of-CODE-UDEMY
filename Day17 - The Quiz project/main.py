from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
