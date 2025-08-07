import random

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "What is the correct way to use *args in a function?",
        "options": ["A. def func(args):", "B. def func(*args):", "C. def func[*args]:", "D. def func(args*):"],
        "answer": "B"
    },
    {
        "question": "What does the random.choice() function do?",
        "options": ["A. Shuffles a list", "B. Chooses a random key from a dictionary", "C. Returns a random element from a sequence", "D. Returns a random integer"],
        "answer": "C"
    },
    {
        "question": "Which of these is a valid Python dictionary?",
        "options": ["A. {1, 2, 3}", "B. [1, 2, 3]", "C. {\"a\": 1, \"b\": 2}", "D. (\"a\", \"b\")"],
        "answer": "C"
    },
    {
        "question": "What is the result of: len([1, 2, 3, 4])?",
        "options": ["A. 4", "B. 3", "C. Error", "D. 5"],
        "answer": "A"
    },
    {
        "question": "What is the correct syntax to cast a string '5' to an integer?",
        "options": ["A. int('5')", "B. str(5)", "C. float(5)", "D. cast('5')"],
        "answer": "A"
    },
    {
        "question": "Which Python data structure is immutable?",
        "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "What is the result of: 'Python'.lower()?",
        "options": ["A. PYTHON", "B. python", "C. Python", "D. error"],
        "answer": "B"
    }
]

valid_options = ["A", "B", "C", "D"]
questions_quantity=4

def checking_answers(questions,userinput,questions_quantity,correct_answers):
    for answer in range(questions_quantity):
        if userinput[answer].upper()==questions[answer]["answer"].upper():
            correct_answers+=1
    return correct_answers
    

while True:
    correct_answers=0
    userinput=[]
    selected_questions = random.sample(questions, questions_quantity)

    for question_num in range(questions_quantity):
        print(selected_questions[question_num]["question"])
        for answer_num in range(4):
            print(selected_questions[question_num]["options"][answer_num], end=" ")
        print()
        answer=input("Witch answer do you pick: ")
        while answer.upper() not in valid_options: 
            answer = input("Invalid. Choose A, B, C, or D: ")
        userinput.append(answer)

    correct_answers=checking_answers(selected_questions,userinput,questions_quantity,correct_answers)
    print(f"You have {correct_answers} out of {questions_quantity} points that's {correct_answers/questions_quantity*100:.0f}%")

    play_again=input("Do you want to play next quizz?(Y/N)")
    if play_again.lower()=="yes"or play_again.lower()=="y":
        continue
    else:
        break
