# TODO asking questions
# TODO checking if the answer was correct
# TODO checking if we are the end of the quiz




class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True    
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number+1}: {current_question.text} (True/False)? ")
        self.question_number += 1
        




         

    



