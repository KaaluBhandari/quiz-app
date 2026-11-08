import random

# Question bank: list of dictionaries
question_bank = [
    {"question": "Which keyword is used to define a function in Python?",
     "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"}, "answer": "B"},
    {"question": 'What is the value of len("Hi")?',
     "options": {"A": "1", "B": "2", "C": "3", "D": "4"}, "answer": "B"},
    {"question": "Which of these data types is mutable in Python?",
     "options": {"A": "tuple", "B": "str", "C": "list", "D": "int"}, "answer": "C"},
    {"question": "Which symbol is used for comments in Python?",
     "options": {"A": "//", "B": "#", "C": "/* */", "D": "--"}, "answer": "B"},
    {"question": "What does the len() function return?",
     "options": {"A": "Sum of elements", "B": "Number of elements", "C": "Largest element", "D": "Data type"}, "answer": "B"},
    {"question": "Which loop is used when the number of iterations is known in advance?",
     "options": {"A": "while", "B": "for", "C": "do-while", "D": "if"}, "answer": "B"},
    {"question": "Which module is used to generate random numbers in Python?",
     "options": {"A": "math", "B": "random", "C": "os", "D": "sys"}, "answer": "B"},
    {"question": "Which of these data types is immutable in Python?",
     "options": {"A": "list", "B": "dict", "C": "set", "D": "tuple"}, "answer": "D"},
    {"question": "Which operator is used for floor division in Python?",
     "options": {"A": "/", "B": "//", "C": "%", "D": "**"}, "answer": "B"},
    {"question": "Which built-in function converts a string into an integer?",
     "options": {"A": "str()", "B": "int()", "C": "float()", "D": "input()"}, "answer": "B"},
]

QUIZ_LENGTH = 3
PASS_MARK_PERCENT = 50
VALID_OPTIONS = ["A", "B", "C", "D"]


def ask_question(q, number):
    while True:
        print(f"\nQ{number}. {q['question']}")
        for key in VALID_OPTIONS:
            print(f"   {key}. {q['options'][key]}")

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer in VALID_OPTIONS:
            break
        print("Invalid option. Enter A, B, C or D.")

    if answer == q["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! Correct answer: {q['answer']}")
        return False


def run_quiz():
    print("=" * 40)
    print("        QUIZ APPLICATION")
    print("=" * 40)

    selected_questions = random.sample(question_bank, QUIZ_LENGTH)

    score = 0
    for i, q in enumerate(selected_questions, start=1):
        if ask_question(q, i):
            score += 1

    total = len(selected_questions)
    percentage = (score / total) * 100
    result = "Pass" if percentage >= PASS_MARK_PERCENT else "Fail"

    print("\n" + "=" * 40)
    print("              RESULT")
    print("=" * 40)
    print(f"Score: {score}/{total} | Percentage: {percentage:.2f}%")
    print(f"Result: {result}")


if __name__ == "__main__":
    run_quiz()