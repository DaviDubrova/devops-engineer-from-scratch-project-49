from brain_games.constants import MIN_NUMBER, MAX_NUMBER
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer
