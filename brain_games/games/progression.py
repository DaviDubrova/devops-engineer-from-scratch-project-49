from brain_games.constants import MIN_NUMBER, TWO, FIVE, TEN, TWENTY
import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question():
    start = random.randint(MIN_NUMBER, TWENTY)
    step = random.randint(TWO, FIVE)
    length = random.randint(FIVE, TEN)

    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
