from question_model import Question_model
from data import question_data
from quiz_brain import QUIZ_BRAIN

QUIZ_BRAIN = QUIZ_BRAIN()

Game_running = True
while Game_running:
    Question = Question_model(question_data).question_extracting(QUIZ_BRAIN.returning_question_number_answer())
    answer = Question_model(question_data).answer_extracting(QUIZ_BRAIN.returning_question_number_answer())
    right_answer = QUIZ_BRAIN.checking_answer(answer=answer)
    if right_answer:
        Game_running = QUIZ_BRAIN.question_overs()

    else:
        Game_running = False
