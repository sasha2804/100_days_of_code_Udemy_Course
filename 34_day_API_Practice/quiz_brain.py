
import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        return f"Q.{self.question_number}: {q_text} (True/False): "
        # self.check_answer(user_answer)
        # self.get_text(q_text)

    def get_text(self, q_text):
        return q_text


    def check_answer(self, user_answer):
        print(user_answer)
        # correct_answer = self.current_question.answer
        correct_answer = self.question_list[self.question_number] 
        if user_answer.lower() == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


#   def next_question(self):
#         current_question = self.question_list[self.question_number]
#         user_input = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)? ")
#         self.check_answer(user_input)
#         self.question_number += 1