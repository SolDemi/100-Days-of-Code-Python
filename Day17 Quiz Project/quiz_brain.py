class QuizBrain:
    def __init__(self, Questions):
        self.question_list = Questions
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, question)

    def check_answer(self, user_answer, question):
        if user_answer == question.answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("That's wrong.")
            print(f"The correct answer is {question.answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")