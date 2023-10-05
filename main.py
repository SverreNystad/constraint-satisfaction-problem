""" The main entrypoint for the application. """

from src.sudoku_solver.sudoku_utils import create_sudoku_csp, print_sudoku_solution

from src.sudoku_solver.visualization import generate_sudoku_image
EASY = "data/easy.txt"
MEDIUM = "data/medium.txt"
HARD = "data/hard.txt"
VERY_HARD = "data/veryhard.txt"
SUPER_HARD = "data/superhard.txt"

def solve_sudoku(filename, title):
    print("Sudoku from file: " + filename)
    sudoku = create_sudoku_csp(filename)
    solution = sudoku.backtracking_search()
    sudoku.print_stats()
    print_sudoku_solution(solution)
    generate_sudoku_image(solution, title)
    print("")

if __name__ == "__main__":
    solve_sudoku(EASY, "EASY")
    solve_sudoku(MEDIUM, "MEDIUM")
    solve_sudoku(HARD, "HARD")
    solve_sudoku(VERY_HARD, "VERY_HARD")
    solve_sudoku(SUPER_HARD, "SUPER_HARD")

