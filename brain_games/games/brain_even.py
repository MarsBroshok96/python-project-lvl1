"""Module with brain even game."""

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    """
    Generate new brain_even task for player.

    Returns:
           Question and correct answer.
    """
    question = random.randint(0, 1000)
    answer = 'no' if question % 2 else 'yes'
    return question, answer
