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
