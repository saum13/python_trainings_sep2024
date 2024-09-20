import csv
import os

QUESTIONS_FILE = 'questions.csv'

class QuestionMaster:
    def __init__(self):
        self.questions = self.load_questions()

    def load_questions(self):
        if os.path.exists(QUESTIONS_FILE):
            with open(QUESTIONS_FILE, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)
        return []

    def save_questions(self):
        with open(QUESTIONS_FILE, 'w', newline='') as csvfile:
            fieldnames = ['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.questions)

    def add_question(self, question, options, correct_option):
        num = len(self.questions) + 1
        new_question = {
            'num': num,
            'question': question,
            'option1': options[0],
            'option2': options[1],
            'option3': options[2],
            'option4': options[3],
            'correctoption': correct_option
        }
        self.questions.append(new_question)
        self.save_questions()

    def search_question(self, num):
        for question in self.questions:
            if int(question['num']) == num:
                return question
        return None

    def delete_question(self, num):
        self.questions = [q for q in self.questions if int(q['num']) != num]
        self.save_questions()

    def modify_question(self, num, new_question_data):
        question = self.search_question(num)
        if question:
            question.update(new_question_data)
            self.save_questions()

    def display_all(self):
        for question in self.questions:
            print(f"{question['num']}. {question['question']}")

def menu():
    master = QuestionMaster()
    while True:
        print("\n1. Add Question")
        print("2. Search Question")
        print("3. Delete Question")
        print("4. Modify Question")
        print("5. Display All Questions")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            question = input("Enter question: ")
            options = [input(f"Option {i+1}: ") for i in range(4)]
            correct_option = input("Correct option (op1/op2/op3/op4): ")
            master.add_question(question, options, correct_option)
        elif choice == '2':
            num = int(input("Enter question number: "))
            result = master.search_question(num)
            print(result if result else "Question not found")
        elif choice == '3':
            num = int(input("Enter question number to delete: "))
            master.delete_question(num)
        elif choice == '4':
            num = int(input("Enter question number to modify: "))
            new_question = input("Enter new question: ")
            options = [input(f"Option {i+1}: ") for i in range(4)]
            correct_option = input("Correct option (op1/op2/op3/op4): ")
            master.modify_question(num, {
                'question': new_question,
                'option1': options[0],
                'option2': options[1],
                'option3': options[2],
                'option4': options[3],
                'correctoption': correct_option
            })
        elif choice == '5':
            master.display_all()
        elif choice == '6':
            break

if __name__ == "__main__":
    menu()
