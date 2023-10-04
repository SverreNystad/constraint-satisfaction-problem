""" The main entrypoint for the application. """

from src.Sudoku_utils import create_sudoku_csp, print_sudoku_solution
from src.map_coloring_util import create_map_coloring_csp
EASY = "data/easy.txt"
MEDIUM = "data/medium.txt"
HARD = "data/hard.txt"
VERY_HARD = "data/veryhard.txt"

def solve_sudoku(filename):
    print("Sudoku from file: " + filename)
    sudoku = create_sudoku_csp(filename)
    solution = sudoku.backtracking_search()
    print_sudoku_solution(solution)
    print("")

if __name__ == "__main__":
    solve_sudoku(EASY)
    solve_sudoku(MEDIUM)
    solve_sudoku(HARD)
    solve_sudoku(VERY_HARD)
