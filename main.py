from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    questions = Question(i['text'],i['answer'])
    question_bank.append(questions)

#print(f"{question.text} and the answer is {question.answer}")

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    print("\n" * 1)

print("You finished the answer, congrats!!!")
print(f"You're final score is: {quiz.score}/{quiz.question_number}")