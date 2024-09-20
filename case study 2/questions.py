import csv

questions = [
    {"num": 1, "question": "10+20 is equal to", "option1": "20", "option2": "30", "option3": "40", "option4": "10", "correctoption": "op2"},
    {"num": 2, "question": "20-10 is equal to", "option1": "20", "option2": "30", "option3": "40", "option4": "10", "correctoption": "op4"},
    {"num": 3, "question": "2*2 is equal to", "option1": "4", "option2": "5", "option3": "6", "option4": "7", "correctoption": "op1"},
    {"num": 4, "question": "5/2 is equal to", "option1": "2.5", "option2": "3", "option3": "6", "option4": "7", "correctoption": "op1"},
    {"num": 5, "question": "Capital of India is", "option1": "Delhi", "option2": "Bangalore", "option3": "Mumbai", "option4": "Chennai", "correctoption": "op1"},
    {"num": 6, "question": "Linux is a", "option1": "Operating System", "option2": "Application", "option3": "Game", "option4": "Antivirus", "correctoption": "op1"}
]

with open('questions.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["num", "question", "option1", "option2", "option3", "option4", "correctoption"])
    writer.writeheader()
    writer.writerows(questions)

print("questions.csv file created successfully.")
