"""Module with brain calc game."""

import operator
import random

RULES = 'What is the result of the expression?'


def get_question_and_answer():
    """
    Generate new brain_calc task for player.

    Returns:
           Question and correct answer.
    """
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = random.choice(list(operations.keys()))
    question = '{0} {1} {2}'.format(first_num, operation, second_num)
    answer = str(operations[operation](first_num, second_num))
    return question, answer
