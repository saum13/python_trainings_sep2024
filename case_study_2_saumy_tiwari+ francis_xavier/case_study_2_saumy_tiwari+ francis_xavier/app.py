import random
from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for using session

QUESTIONS_FILE = 'questions.csv'
LEADERBOARD_FILE = 'leaderboard.csv'

# Load questions from CSV
def load_questions():
    questions = []
    with open(QUESTIONS_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

# Randomly select 7 questions, re-assigning serial numbers
def select_questions():
    questions = load_questions()
    selected_questions = random.sample(questions, 7)
    # Reassign serial numbers (1, 2, 3,... instead of the original numbers)
    for i, question in enumerate(selected_questions, start=1):
        question['num'] = str(i)
    return selected_questions

# Save participant's score to leaderboard CSV
def save_score(name, university, score):
    with open(LEADERBOARD_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, university, score])

# Route for homepage (starting the quiz)
@app.route('/', methods=['GET', 'POST'])
def exam():
    if request.method == 'POST':
        name = request.form['name']
        university = request.form['university']
        user_answers = []

        # Get the questions from session
        questions = session.get('questions', [])

        for question in questions:
            answer = request.form.get(f'question_{question["num"]}', '')
            user_answers.append(answer)

        # Calculate score correctly
        score = 0
        for i, question in enumerate(questions):
            correct_answer = question['correctoption'][-1]  # Get the last character (1, 2, 3, or 4)
            if user_answers[i] == correct_answer:
                score += 1

        # Save score and redirect to result page
        save_score(name, university, score)
        return redirect(url_for('result', name=name, university=university, score=score, total=len(questions)))

    # Select and store 7 random questions in session
    questions = select_questions()
    session['questions'] = questions
    return render_template('exam.html', questions=questions)

# Route for displaying the result after the exam
@app.route('/result')
def result():
    name = request.args.get('name')
    university = request.args.get('university')
    score = request.args.get('score')
    total = request.args.get('total')  # Get the total number of questions
    return render_template('result.html', name=name, university=university, score=score, total=total)

# Route for displaying the leaderboard
@app.route('/leaderboard')
def leaderboard():
    try:
        with open(LEADERBOARD_FILE, mode='r') as file:
            reader = csv.reader(file)
            leaderboard = sorted(reader, key=lambda row: int(row[2]), reverse=True)[:5]
    except FileNotFoundError:
        leaderboard = []

    return render_template('leaderboard.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
