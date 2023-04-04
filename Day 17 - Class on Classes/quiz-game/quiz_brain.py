class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.last_answer = True
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            current_question_text = current_question.text
            current_question_answer = current_question.answer
            user_answer = input(
                f"Q.{self.question_number + 1}: {current_question_text} (True/False): ")
            self.check_answer(user_answer, current_question_answer)
        else:
            print("You've completed the quiz.")
            return (print(f"Your final score was: {self.score} correct answers out of a total of {len(self.question_list)} questions."))
    
    def check_answer(self, user_answer, current_question_answer):
        if user_answer.lower() == current_question_answer.lower():
            print("You got it right!")
            print("\n")
            self.question_number += 1
            self.score += 1
            self.next_question()
        else:
            self.last_answer = False
            print("That's wrong.")
            print("You've failed miserably.")
            return (print(f"Your final score was: {self.score} correct answers out of a total of {len(self.question_list)} questions."))


