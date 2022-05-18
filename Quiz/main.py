import random
from data import question_data
from question_model import Question


question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"], i["justification"]))

score = 0
proceed = True
question_count = 1
while proceed:
    if len(question_bank) == 0:
        print(f"You have answered all {score} questions correctly! You are truly a Pokemon master!")
        break
    query = random.choice(question_bank)
    print(f"Question {question_count}: {query.display_text()}")
    question_count += 1
    user_answer = input("What is your answer to this question? (True/False)\n")
    if query.check(user_answer):
        score += 1
        print(f"Congratulations! You got this question correct! Current score: {score}")
        query.display_justification()
        question_bank.remove(query)
        continue
    else:
        print(f"Sorry you got it wrong. Your final score is {score}")
        query.display_justification()
        break
