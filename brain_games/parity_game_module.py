"""Module with funcs for brain-even game."""

import random

import prompt


def is_even():
    """Test user's knowledge about parity of numbers.

    Returns:
           result of game
    """
    number = random.randint(0, 1000)
    win_in_row = 0

    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def user_answer():
        """Get answer from user about number parity.

        Returns:
               user answer
        """
        print('Question: {0}'.format(number))
        return prompt.string('Your answer: ')

    def correct_answer():
        """Geting correct answer about number parity.

        Returns:
               'yes' or 'no' in depends of number parity.
        """
        if number % 2 == 0:
            return 'yes'
        return 'no'

    user_answ = user_answer()
    correct_answ = correct_answer()

    while user_answ == correct_answ:

        print('Correct!')
        win_in_row += 1

        if win_in_row < 3:
            number = random.randint(0, 1000)
            user_answ = user_answer()
            correct_answ = correct_answer()
        else:
            return print('Congratulations, {0}!'.format(username))

    print(
        "'{0}' is wrong answer ;(.".format(user_answ)
        +
        "Correct answer was '{0}'".format(correct_answ)
        +
        "\nLet's try again, {0}!".format(username),
    )
