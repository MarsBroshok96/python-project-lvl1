"""Module with brain gcd game."""

import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_progression():
    """
    Generate simple arithmetic progression with choosen hidden index.

    Returns:
            Simple arithmetic progression with choosen hidden index.
    """
    start = random.randint(0, 100)
    step = random.randint(1, 100)
    length = random.randint(5, 20)   # 5, 20: min and max length
    end = (start + step * length)
    progression = list(range(start, end, step))
    hidden_index = random.randrange(0, length)
    return (progression, hidden_index)


def get_question_and_answer():
    """
    Generate new brain_progression task for player.

    Returns:
           Question and correct answer.
    """
    (progression, hidden_index) = generate_progression()
    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = progression
    return question, answer
