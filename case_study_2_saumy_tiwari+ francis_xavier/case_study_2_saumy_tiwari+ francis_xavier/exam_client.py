import csv
import datetime

QUESTIONS_FILE = 'questions.csv'
LEADERBOARD_FILE = 'leaderboard.csv'

def load_questions():
    questions = []
    with open(QUESTIONS_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

def save_score(name, university, score):
    # Read the current leaderboard
    leaderboard = []
    try:
        with open(LEADERBOARD_FILE, mode='r') as file:
            reader = csv.reader(file)
            leaderboard = list(reader)
    except FileNotFoundError:
        pass

    # Add the new score
    leaderboard.append([name, university, str(score)])

    # Sort by score and keep only the top 5 entries
    leaderboard = sorted(leaderboard, key=lambda row: int(row[2]), reverse=True)[:5]

    # Write the updated leaderboard back to the file
    with open(LEADERBOARD_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)


def display_leaderboard():
    try:
        with open(LEADERBOARD_FILE, mode='r') as file:
            reader = csv.reader(file)
            leaderboard = sorted(reader, key=lambda row: int(row[2]), reverse=True)[:5]
            print("\nLeaderboard:")
            for rank, entry in enumerate(leaderboard, start=1):
                print(f"{rank}. {entry[0]} ({entry[1]}) - {entry[2]} points")
    except FileNotFoundError:
        print("No scores available yet.")

def start_exam():
    name = input("\nEnter student name: ")
    university = input("\nEnter university: ")
    
    questions = load_questions()
    score = 0
    
    for question in questions:
        print(f"\n{question['num']}) {question['question']} \n")
        print(f"1) {question['option1'][4:]}")
        print(f"2) {question['option2'][4:]}")
        print(f"3) {question['option3'][4:]}")
        print(f"4) {question['option4'][4:]}")
        
        # Validate user input
        while True:
            answer = input("\nEnter your choice (1/2/3/4): ")
            if answer in ['1', '2', '3', '4']:
                break
            else:
                print("\nInvalid Option, please try again.")
        
        if answer == question['correctoption'][-1]:
            score += 1
    
    print(f"\nStudent name = {name}")
    print(f"University = {university}")
    print(f"Marks scored = {score} out of {len(questions)}")
    
    save_score(name, university, score)

def menu():
    while True:
        print("\n1) Start Exam")
        print("2) View Leaderboard")
        print("3) Exit \n")
        choice = input("Enter choice: ")
        
        if choice == '1':
            start_exam()
        elif choice == '2':
            display_leaderboard()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
