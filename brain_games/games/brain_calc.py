"""Module with brain calc game."""

import random

RULES = 'What is the result of the expression?'


def generate_task():
    """
    Generate new brain_calc task for player.

    Returns:
           Task and correct answer.
    """
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    num_of_operator = random.randint(1, 3)

    if num_of_operator == 1:
        task = '{0} + {1}'.format(first_num, second_num)
        answer = first_num + second_num
    elif num_of_operator == 2:
        task = '{0} - {1}'.format(first_num, second_num)
        answer = first_num - second_num
    else:
        task = '{0} * {1}'.format(first_num, second_num)
        answer = first_num * second_num
    return (task, str(answer))
