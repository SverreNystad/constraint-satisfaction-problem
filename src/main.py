""" The main entrypoint for the application. """

from Assignment import create_sudoku_csp


def hello_world() -> str:
    """ Returns a friendly greeting. """
    return "Hello World!"



EASY = "data/easy.txt"
MEDIUM = "data/medium.txt"
HARD = "data/hard.txt"
VERY_HARD = "data/veryhard.txt"

easy_sudoku = create_sudoku_csp(EASY)

medium_sudoku = create_sudoku_csp(MEDIUM)
hard_sudoku = create_sudoku_csp(HARD)
very_hard_sudoku = create_sudoku_csp(VERY_HARD)
