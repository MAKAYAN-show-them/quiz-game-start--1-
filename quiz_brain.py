from question_model import Question_model
from data import question_data

class QUIZ_BRAIN:
    def __init__(self) -> None:
        self.question_number = 0
        self.point = 0

    def returning_question_number_answer(self):
        return self.question_number
    
    def taking_input_user(self,question):
        wrong_answer = True
        while wrong_answer:
            user_input = input(f"{question} Answer in True & False only.\n").title()
            if user_input in ["True" , "False"]:
                wrong_answer = False
                return user_input
            else:
                print("Give Right Input")
    
    def checking_answer(self,answer):
        if answer == self.taking_input_user(question=Question_model(question_data).question_extracting(self.returning_question_number_answer())):
            self.point += 1
            print("Right Answer")
            print(f"Your Points {self.point}/{self.question_number + 1}")
            return True
        
        else:
            print(f"Wrong Answer. The correct answer was {answer}")
            print(f"Your Points {self.point}/{self.question_number + 1}")
            return False
        
    def question_overs(self):
        if (Question_model(question_data).total_question_list() -1) == self.question_number:
            print("You give all the answer correct! Congratulation")
            return False
        
        else:
            self.question_number += 1
            return True        

                
        
    