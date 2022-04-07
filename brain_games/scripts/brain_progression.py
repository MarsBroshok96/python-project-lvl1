"""Test user's arithmetic and logic skills."""
from brain_games.engine import run_game
from brain_games.games import brain_progression


def main():
    """Name as main."""
    run_game(brain_progression)


if __name__ == '__main__':
    main()
