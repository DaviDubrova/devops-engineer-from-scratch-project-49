from brain_games.main import main
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    main()
