import csv
import datetime

QUESTIONS_FILE = 'questions.csv'
LEADERBOARD_FILE = 'leaderboard.csv'

class ExamClient:
    def __init__(self, student_name, university):
        self.student_name = student_name
        self.university = university
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        with open(QUESTIONS_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def conduct_exam(self):
        for question in self.questions:
            print(f"\nQ{question['num']}: {question['question']}")
            print(f"1) {question['option1']}")
            print(f"2) {question['option2']}")
            print(f"3) {question['option3']}")
            print(f"4) {question['option4']}")

            # Loop until a valid choice is provided
            while True:
                answer = input("Enter your choice (1/2/3/4): ")

                # Check if the input is valid (should be 1, 2, 3, or 4)
                if answer in ['1', '2', '3', '4']:
                    break
                else:
                    print("Invalid response. Please try again by choosing 1, 2, 3, or 4.")

            # Check if the answer is correct
            if f"op{answer}" == question['correctoption']:
                self.score += 1

        self.display_result()

    def display_result(self):
        current_time = datetime.datetime.now().strftime('%d/%b/%Y %H:%M:%S')
        print(f"\nStudent Name: {self.student_name}")
        print(f"University: {self.university}")
        print(f"Marks scored: {self.score}/{len(self.questions)}")
        print(f"Date and Time: {current_time}")

        self.update_leaderboard(current_time)

    def update_leaderboard(self, current_time):
        leaderboard = self.load_leaderboard()

        # Add the current player's score
        leaderboard.append({
            'name': self.student_name,
            'university': self.university,
            'score': self.score,  # Store score as an integer
            'datetime': current_time
        })

        # Sort leaderboard by score (descending) and datetime (ascending)
        leaderboard = sorted(leaderboard, key=lambda x: (-int(x['score']), x['datetime']))  # Convert 'score' to int

        # Keep only the top 5 players
        leaderboard = leaderboard[:5]

        # Save the updated leaderboard
        self.save_leaderboard(leaderboard)

        # Display the top 5 players
        print("\nLeaderboard (Top 5 Players):")
        for idx, entry in enumerate(leaderboard, 1):
            print(f"{idx}. {entry['name']} from {entry['university']} scored {entry['score']} on {entry['datetime']}")

    def load_leaderboard(self):
        try:
            with open(LEADERBOARD_FILE, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)
        except FileNotFoundError:
            return []

    def save_leaderboard(self, leaderboard):
        with open(LEADERBOARD_FILE, 'w', newline='') as csvfile:
            fieldnames = ['name', 'university', 'score', 'datetime']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(leaderboard)

if __name__ == "__main__":
    print("Welcome to the Online Exam")
    print(f"Today's date and time: {datetime.datetime.now().strftime('%d/%b/%Y %H:%M:%S')}")
    student_name = input("Enter your name: ")
    university = input("Enter your university: ")

    exam_client = ExamClient(student_name, university)
    exam_client.conduct_exam()
