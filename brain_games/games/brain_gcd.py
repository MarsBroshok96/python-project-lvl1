"""Module with brain gcd game."""

import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_task():
    """
    Generate new brain_gcd task for player.

    Returns:
           Task and correct answer.
    """
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    task = '{0} {1}'.format(first_number, second_number)

    if first_number < second_number:
        max_possible_gcd = first_number
    else:
        max_possible_gcd = second_number

    for i in range(max_possible_gcd, 0, -1):
        if first_number % i == 0 and second_number % i == 0:
            answer = i
            break
    return (task, str(answer))
