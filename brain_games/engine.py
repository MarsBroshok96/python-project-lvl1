"""Module with basic architecture for brain-games."""

import prompt


def greet_and_get_name():
    """
    Greet player, show rules and return players name.

    Returns:
            Player's name.
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
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


def run_game(game):
    """
    Show rules of choosen game and run it.

    Args:
        game: One of game modules.

    Returns:
           Victory or defeat expression.
    """
    player_name = greet_and_get_name()
    print(game.RULES)
    (task, correct_answer) = game.generate_task()
    player_answer = get_player_answer(task)

    win_in_row = 0

    while player_answer == correct_answer:

        print('Correct!')
        win_in_row += 1

        if win_in_row < 3:
            (task, correct_answer) = game.generate_task()
            player_answer = get_player_answer(task)
        else:
            return print('Congratulations, {0}!'.format(player_name))
    print(
        "'{0}' is wrong answer ;(."
        "Correct answer was '{1}'\nLet's try again, "
        '{2}!'.format(player_answer, correct_answer, player_name),
    )
