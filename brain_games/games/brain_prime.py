"""Module with brain prime game."""

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    """
    Generate new brain_prime task for player.

    Returns:
           Question and correct asnwer.
    """
    question = random.randint(1, 1000)

    if question % 2 == 0:
        answer = 'no'
        return question, answer
    max_possible_prime = int((question - 1) / 2)

    for i in range(max_possible_prime, 1, -1):
        if question % i == 0:
            answer = 'no'
            break
        answer = 'yes'
    return question, answer
