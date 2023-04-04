from question_model import Question
from data import question_data_2
from quiz_brain import QuizBrain

question_bank = []

for question in question_data_2:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
quiz.next_question()
