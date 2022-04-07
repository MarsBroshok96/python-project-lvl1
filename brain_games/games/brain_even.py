"""Module with brain even game."""

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task():
    """
    Generate new brain_even task for player.

    Returns:
           Task and correct answer.
    """
    task = random.randint(0, 1000)

    if task % 2 == 0:
        answer = 'yes'
        return (task, answer)
    answer = 'no'
    return (task, answer)
