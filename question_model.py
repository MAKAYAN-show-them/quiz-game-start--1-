from data import question_data

class Question_model:
    def __init__(self,question_answer_list) -> None:
        self.question_answer_list = question_answer_list
        
    def question_extracting(self,question_number):
        return self.question_answer_list[question_number]["text"]
    
    def answer_extracting(self,answer_number):
        return self.question_answer_list[answer_number]["answer"]
    
    def total_question_list(self):
        return len(self.question_answer_list)

        
        
