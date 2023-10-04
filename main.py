""" The main entrypoint for the application. """

from src.Sudoku_utils import create_sudoku_csp, print_sudoku_solution

EASY = "data/easy.txt"
MEDIUM = "data/medium.txt"
HARD = "data/hard.txt"
VERY_HARD = "data/veryhard.txt"



print("Easy Sudoku")
easy_sudoku = create_sudoku_csp(EASY)
solution = easy_sudoku.backtracking_search()
print_sudoku_solution(solution)

print("Medium Sudoku")
medium_sudoku = create_sudoku_csp(MEDIUM)
solution = medium_sudoku.backtracking_search()
print_sudoku_solution(solution)

print("Hard Sudoku")
hard_sudoku = create_sudoku_csp(HARD)
solution = hard_sudoku.backtracking_search()
print(f"solution = {solution}")
print(f"hard_sudoku solution = {solution}")
print_sudoku_solution(solution)

print("Very Hard Sudoku")
very_hard_sudoku = create_sudoku_csp(VERY_HARD)
solution = very_hard_sudoku.backtracking_search()
print_sudoku_solution(solution)

