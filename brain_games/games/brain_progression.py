"""Module with brain-progression game."""

import random

RULES = 'What number is missing in the progression?'


def generate_task():
    """
    Generate new brain_progression task for player.

    Returns:
           Task and correct answer.
    """
    def generate_prog():
        """
        Generate simple arithmetic progression.

        Returns:
               start point, end point and step for progression.
        """
        start = random.randint(0, 100)
        step = random.randint(1, 100)
        length = random.randint(5, 20)   # 5, 20: min and max length
        end = (start + step * length) + 1
        return (start, end, step)

    (start, end, step) = generate_prog()
    progression = list(range(start, end, step))
    answer = random.choice(progression)

    task = ''

    for i in range(start, end, step):
        if i == answer:
            i = '..'
        task = '{0}{1} '.format(task, str(i))
    return (task, str(answer))
