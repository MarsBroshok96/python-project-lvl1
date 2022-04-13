"""Module with brain gcd game."""

import random

RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    """
    Calculate GCD of two numbers with subtraction method.

    Returns:
           GCD of two numbers.

    Args:
        first_number: number
        second_number: other number
    """
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return str(first_number)


def get_question_and_answer():
    """
    Generate new brain_gcd task for player.

    Returns:
           Question and correct answer.
    """
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    question = '{0} {1}'.format(first_number, second_number)
    answer = get_gcd(first_number, second_number)

    return question, answer
