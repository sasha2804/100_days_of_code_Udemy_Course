from question_model_day_17 import Question
from data_day_17 import question_data
from quiz_brain_day_17 import QuizBrain

question_bank = []

for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()



