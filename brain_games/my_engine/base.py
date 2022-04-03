"""Module with basic architecture for brain-games."""

import random

import prompt


def greet_and_get_name(rules):
    """
    Greet player, show rules and return players name.

    Args:
        rules: Rules of the game.

    Returns:
           Player's name.
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    print(rules)
    return player_name


def get_player_answer(task):
    """
    Get answer from player.

    Args:
        task: Expression with task for player.

    Returns:
           Player answer.
    """
    print('Question: {0}'.format(task))
    return prompt.string('Your asnwer: ')


def generate_task_calc():
    """
    Generate new brain_calc task for player.

    Returns:
           Task and correct answer.
    """
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    num_of_operator = random.randint(1, 3)

    if num_of_operator == 1:
        task = '{0} + {1}'.format(first_num, second_num)
        answer = first_num + second_num
    elif num_of_operator == 2:
        task = '{0} - {1}'.format(first_num, second_num)
        answer = first_num - second_num
    else:
        task = '{0} * {1}'.format(first_num, second_num)
        answer = first_num * second_num
    return (task, str(answer))


def generate_task_gcd():
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


def generate_task_progression():
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
        task = '{0} {1}'.format(task, str(i))
    return (task, str(answer))


def generate_task_prime():
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
