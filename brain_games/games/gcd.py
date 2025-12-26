from brain_games.constants import MIN_NUMBER, MAX_NUMBER
import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
