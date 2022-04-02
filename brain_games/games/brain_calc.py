"""Module with brain calc game."""

from brain_games.my_engine.base import (
    generate_task_calc,
    get_player_answer,
    greet_and_get_name,
)

rules = 'What is the result of the expression?'


def victory_conditions():
    """Logic of victory and defeat + scoring.

    Returns:
           Winner or loooser expression
    """
    player_name = greet_and_get_name(rules)
    (task, correct_answer) = generate_task_calc()
    player_answer = get_player_answer(task)

    win_in_row = 0

    while player_answer == correct_answer:

        print('Correct!')
        win_in_row += 1

        if win_in_row < 3:
            (task, correct_answer) = generate_task_calc()
            player_answer = get_player_answer(task)
        else:
            return print('Congratulations, {0}!'.format(player_name))
    print(
        "'{0}' is wrong answer ;(.".format(player_answer)
        +
        "Correct answer was '{0}'".format(correct_answer)
        +
        "\nLet's try again, {0}!".format(player_name),
    )
