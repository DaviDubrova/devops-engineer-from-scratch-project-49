import prompt
MAX_ROUNDS = 3

def run(game):
    """Сотый запуск игры."""

    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.get_question()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {user_name}!")
            return
        print("Correct!")

    print(f"Congratulations, {user_name}!")
