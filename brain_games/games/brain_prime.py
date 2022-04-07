"""Module with brain prime game."""

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_task():
    """
    Generate new brain_prime task for player.

    Returns:
           Task and correct asnwer.
    """
    task = random.randint(1, 1000)

    if task % 2 == 0:
        answer = 'no'
        return (task, answer)
    max_possible_prime = int((task - 1) / 2)

    for i in range(max_possible_prime, 1, -1):
        if task % i == 0:
            answer = 'no'
            break
        answer = 'yes'
    return (task, answer)
