# Quiz Application

**Course:** Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)
**Name:** Shreyansh Kumar Singh
**ERP No.:** RU-26-01965
**Section:** O
**PS No.:** 88

---

## 1. Problem Statement

Develop a console-based quiz application that asks multiple-choice questions
randomly from a question bank, checks the user's answers, keeps score, and
displays the final result.

- **Language:** Python 3
- **Concepts used:** Lists, Dictionaries, Loops, Random module

---

## 2. Approach

The question bank is stored as a **list of dictionaries**. Each dictionary
holds a question, its four options (A-D), and the correct answer letter.
This structure keeps all the data for one question grouped together, and
makes it easy to loop through and randomly sample from.

The program flow is:

1. Randomly select 3 unique questions from the bank of 10 using
   `random.sample()`.
2. Display each question with its four options.
3. Accept the user's answer, re-prompting if the input is not A, B, C, or D.
4. Compare the answer to the correct one, update the score, and show
   immediate feedback (Correct / Wrong + correct answer).
5. After all questions are answered, calculate the score, percentage, and
   Pass/Fail result (pass mark: 50%).

---

## 3. Code Structure

| Component | Purpose |
|---|---|
| `question_bank` | List of 10 dictionaries, each representing one question |
| `ask_question(q, number)` | Displays one question, validates input, returns True/False |
| `run_quiz()` | Selects questions, runs the quiz loop, calculates and prints the result |
| `random.sample()` | Picks 3 unique random questions from the bank (no repeats) |

### Why a list of dictionaries?

Each question needs several related pieces of data (text, options, correct
answer) bundled together. A dictionary keeps these associated by key, and a
list of dictionaries lets the program loop through and randomly sample from
many questions easily.

### Why `random.sample()` instead of `random.choice()`?

`random.choice()` can select the same item more than once across repeated
calls, which could repeat a question in the same quiz. `random.sample()`
guarantees unique selections, so no question is asked twice in one run.

### Input validation

The answer-collection step runs inside a `while True` loop that only breaks
once a valid option (A/B/C/D) is entered. This prevents the program from
crashing or accepting invalid input, and matches Test Case 3 from the
project brief.

---

## 4. How to Run

```bash
python quiz_app.py
```

Follow the on-screen prompts and answer each question with A, B, C, or D.

---

## 5. Test Cases

| Test Case | Input | Expected Output | Result |
|---|---|---|---|
| Normal Input | B, B, C | Score: 3/3, 100.00%, Pass | Pass |
| Boundary / All Wrong | A, A, A | Score: 0/3, 0.00%, Fail, shows correct answers | Pass |
| Invalid Input | E, then B (Q1); B, C (Q2-3) | Invalid option message, question re-asked, then 3/3 Pass | Pass |
| Mixed Valid Scenario | B, A, C | Score: 2/3, 66.67%, Pass, shows Q2 wrong answer | Pass |

---

## 6. Sample Output

```
========================================
        QUIZ APPLICATION
========================================

Q1. Which keyword is used to define a function in Python?
   A. func
   B. def
   C. function
   D. lambda
Your answer (A/B/C/D): B
Correct!

Q2. What is the value of len("Hi")?
   A. 1
   B. 2
   C. 3
   D. 4
Your answer (A/B/C/D): B
Correct!

Q3. Which of these data types is mutable in Python?
   A. tuple
   B. str
   C. list
   D. int
Your answer (A/B/C/D): C
Correct!

========================================
              RESULT
========================================
Score: 3/3 | Percentage: 100.00%
Result: Pass
```

---

## 7. Conclusion

This project demonstrates core Python programming concepts (lists,
dictionaries, loops, conditional logic, and the `random` module) applied
to build a functional, interactive console application with input
validation and automated scoring.