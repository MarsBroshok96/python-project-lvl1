"""Test user's GCD search skills."""
from brain_games.engine import run_game
from brain_games.games import brain_gcd


def main():
    """Name as main."""
    run_game(brain_gcd)


if __name__ == '__main__':
    main()
