class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self):
        print(self.question)
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")
        user_answer = int(input("Choose the correct option: "))
        return user_answer == self.answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for question in self.questions:
            if question.ask():
                self.score += 1
                print("Correct!\n")
            else:
                print("Wrong answer.\n")
        print(f"Your final score: {self.score}/{len(self.questions)}")

# Example Usage
if __name__ == "__main__":
    quiz = Quiz()
    quiz.add_question(Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], 3))
    quiz.add_question(Question("2 + 2 = ?", ["3", "4", "5", "6"], 2))
    quiz.start()
