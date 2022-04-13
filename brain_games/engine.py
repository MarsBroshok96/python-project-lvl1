"""Module with basic architecture for brain-games."""

import prompt


def run_game(game):
    """
    Show rules of choosen game and run it.

    Args:
        game: One of game modules.

    Returns:
           Victory or defeat expression.
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))

    print(game.RULES)
    (question, correct_answer) = game.get_question_and_answer()

    game_rounds_count = 3

    for _ in range(0, game_rounds_count):
        (question, correct_answer) = game.get_question_and_answer()
        print('Question: {0}'.format(question))
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer ;(."
                "Correct answer was '{1}'\nLet's try again, "
                '{2}!'.format(player_answer, correct_answer, player_name),
            )
            return
    print('Congratulations, {0}!'.format(player_name))
