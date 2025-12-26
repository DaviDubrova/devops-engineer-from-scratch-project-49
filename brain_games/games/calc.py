from brain_games.constants import MIN_NUMBER, TWENTY
import random
import operator

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question():
    num1 = random.randint(MIN_NUMBER, TWENTY)
    num2 = random.randint(MIN_NUMBER, TWENTY)
    operation = random.choice(list(OPERATIONS.keys()))
    question = f"{num1} {operation} {num2}"
    correct_answer = OPERATIONS[operation](num1, num2)
    return question, str(correct_answer)
