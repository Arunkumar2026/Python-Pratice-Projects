# This is a Quiz App program


def quiz():
    questions = [
    {
        "question": "Which language is known as the 'mother of all programming languages'?",
        "options": ["A. C", "B. Python", "C. Java", "D. Assembly"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit",
                    "C. Computer Personal Unit", "D. Coutrol Power Unit"],
        "answer": "B"
    },
    {
        "question": "Which data structure uses LIFO?",
        "options": ["A, Queue", "B. Linked List", "C. Stack", "D. Tree"],
        "answer": "C"
    },
    {
        "question": "Which company developed Python?",
        "options":["A. Microsoft", "B. Google", "C. Bell labs", "D. Python Software Foundtion"],
        "answer": "D"
    }
]
    score = 0
    print('\nWelcome to the Quiz Master')
    print('Answer the questions by just typing A,B,C or D\n')

    for i,q in enumerate(questions, start=1):
        print(f'{i}: {q["question"]}')

        for option in q['options']:
            print(option)
        answer = input('Your Answer: ').strip().upper()

        if answer == q['answer']:
            print('Correct\n')
            score += 1
        else:
            print(f'Wrong! Correct Answer:{q["answer"]}\n')

    total = len(questions)
    print(f'Quiz Over! You Scored: {score}/{total}')

    percentage = (score / total) * 100

    print(f'Your Percentage: {percentage:.2f}%')

    if percentage == 100:
        print('Excellent')
    elif percentage >= 60:
        print('Good Job')
    else:
        print('Keep Prcticing')

    retry = input('\n Do you want to play again? (yes/no)').lower()

    if retry == "yes":
        quiz()


quiz()





