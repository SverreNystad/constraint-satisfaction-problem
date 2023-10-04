""" The main entrypoint for the application. """

from src.Sudoku_utils import create_sudoku_csp, print_sudoku_solution

EASY = "data/easy.txt"
MEDIUM = "data/medium.txt"
HARD = "data/hard.txt"
VERY_HARD = "data/veryhard.txt"

easy_sudoku = create_sudoku_csp(EASY)

medium_sudoku = create_sudoku_csp(MEDIUM)
hard_sudoku = create_sudoku_csp(HARD)
very_hard_sudoku = create_sudoku_csp(VERY_HARD)


def solve_sodoku(difficulty: str):
    """ Solves the given sudoku. """
    # Arange the sudoku
    csp = create_sudoku_csp()
    # Solve the sudoku
    csp.backtracking_search()
    # Print the solution
    print_sudoku_solution(csp)
