"""Test user's knowledge about prime numbers."""
from brain_games.engine import run_game
from brain_games.games import brain_prime


def main():
    """Name as main."""
    run_game(brain_prime)


if __name__ == '__main__':
    main()
