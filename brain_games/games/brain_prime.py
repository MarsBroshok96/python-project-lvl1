"""Module with brain prime game."""

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Check the number for prime property.

    Args:
        number: any number

    Returns:
          Boolean
    """
    if number <= 1:
        return False
    div = 2
    while div <= number // 2:
        if not number % div:
            return False
        div += 1
    return True


def get_question_and_answer():
    """
    Generate new brain_prime task for player.

    Returns:
           Question and correct asnwer.
    """
    question = random.randint(1, 1000)

    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
