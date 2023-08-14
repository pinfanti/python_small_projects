from question_model import Question
from data import quiz_data
from quiz_brain import QuizBrain

counter = 0
question_bank = []
for question in quiz_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
user_answer = quiz.next_question()
while quiz.still_has_questions():
    counter+=1
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was:{counter}/{len(question_bank)}")