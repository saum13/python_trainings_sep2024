import csv

QUESTIONS_FILE = 'questions.csv'

def load_questions():
    questions = []
    try:
        with open(QUESTIONS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row)
    except FileNotFoundError:
        print("Questions file not found, starting with an empty set.")
    return questions

def save_questions(questions):
    with open(QUESTIONS_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption'])
        writer.writeheader()
        for q in questions:
            writer.writerow(q)

def add_question(questions):
    num = len(questions) + 1
    question = input("Enter the question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")
    correctoption = input("Enter correct option (e.g., op1, op2): ")
    
    new_question = {
        'num': num,
        'question': question,
        'option1': f'op1={option1}',
        'option2': f'op2={option2}',
        'option3': f'op3={option3}',
        'option4': f'op4={option4}',
        'correctoption': correctoption
    }
    questions.append(new_question)
    save_questions(questions)
    print("Question added successfully!")

def display_questions(questions):
    for question in questions:
        print(f"{question['num']}: {question['question']} ({question['correctoption']})")

def menu():
    questions = load_questions()
    while True:
        print("\n1) Add a question")
        print("2) Display all questions")
        print("3) Exit \n")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_question(questions)
        elif choice == '2':
            display_questions(questions)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
