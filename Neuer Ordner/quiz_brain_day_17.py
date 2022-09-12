# TODO asking questions
# TODO checking if the answer was correct
# TODO checking if we are the end of the quiz




class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.answer_number = 0
        self.score = 0      
        self.question_list = question_list
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True 
   
    def check_answer(self, user_input):
        current_answer = self.question_list[self.question_number]        
        if user_input.lower() == current_answer.answer.lower():
            print(f"You got it right! \nThe correct answer was: {current_answer.answer}.")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number+1}")
        else:
            print(f"That's wrong.\nThe correct answer was: {current_answer.answer}")
            print(f"Your score is {self.score}/{self.question_number+1}")
    

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_input = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)? ")
        self.check_answer(user_input)
        self.question_number += 1
    
    def show_result(self):
        print("\n\nYou have completed the quiz")
        print(f"Your final score was: {self.score}/{len(self.question_list)}")
        
        





         

    



