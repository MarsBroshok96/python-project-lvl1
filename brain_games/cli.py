# #!/usr/bin/env python

"""Module with func for step3."""

import prompt


def welcome_user():
    """Ask a username."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    print('smth')
# other statements
