import json
import time
import random

# Load questions from file
with open("questions.json", "r") as file:
    questions = json.load(file)

score = 0
time_limit = 10   # seconds per question

print("=== Quiz Game ===")
print("You have", time_limit, "seconds per question\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    start_time = time.time()

    answer = input("Your answer: ").upper()

    end_time = time.time()
    time_taken = end_time - start_time

    # Check timer
    if time_taken > time_limit:
        print("Time is up!\n")
        continue

    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("Quiz Finished!")
print("Your Score:", score, "/", len(questions))

random.shuffle(questions)
