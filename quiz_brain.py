class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.user_score = 0

    def has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            print("Correct!")
            self.user_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.user_score}/{self.question_num}")
        print("")