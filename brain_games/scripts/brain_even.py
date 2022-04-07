"""Test user's knowledge about numbers parity."""
from brain_games.engine import run_game
from brain_games.games import brain_even


def main():
    """Name as main."""
    run_game(brain_even)


if __name__ == '__main__':
    main()
