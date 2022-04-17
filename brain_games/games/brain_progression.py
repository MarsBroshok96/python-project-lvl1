"""Module with brain gcd game."""

import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_progression():
    """
    Generate simple arithmetic progression.

    Returns:
            Simple arithmetic progression with it length.
    """
    start = random.randint(0, 100)
    step = random.randint(1, 100)
    length = random.randint(5, 20)   # 5, 20: min and max length
    end = (start + step * length)
    progression = list(range(start, end, step))
    return (progression, length)


def get_question_and_answer():
    """
    Generate new brain_progression task for player.

    Returns:
           Question and correct answer.
    """
    (progression, length) = generate_progression()
    hidden_index = random.randrange(0, length)
    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    str_progression = [str(i) for i in progression]
    question = ' '.join(str_progression)
    return question, answer
