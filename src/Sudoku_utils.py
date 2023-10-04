'''
All given Sudoku utils.
'''

from src.Assignment import CSP

def create_sudoku_csp(filename: str) -> CSP:
    """Instantiate a CSP representing the Sudoku board found in the text
    file named 'filename' in the current directory.

    Parameters
    ----------
    filename : str
        Filename of the Sudoku board to solve

    Returns
    -------
    CSP
        A CSP instance
    """
    csp = CSP()
    board = list(map(lambda x: x.strip(), open(filename, 'r')))

    for row in range(9):
        for col in range(9):
            if board[row][col] == '0':
                csp.add_variable('%d-%d' % (row, col), list(map(str,
                                                                range(1, 10))))
            else:
                csp.add_variable('%d-%d' % (row, col), [board[row][col]])

    for row in range(9):
        csp.add_all_different_constraint(['%d-%d' % (row, col)
                                          for col in range(9)])
    for col in range(9):
        csp.add_all_different_constraint(['%d-%d' % (row, col)
                                         for row in range(9)])
    for box_row in range(3):
        for box_col in range(3):
            cells = []
            for row in range(box_row * 3, (box_row + 1) * 3):
                for col in range(box_col * 3, (box_col + 1) * 3):
                    cells.append('%d-%d' % (row, col))
            csp.add_all_different_constraint(cells)

    return csp


def print_sudoku_solution(solution):
    """Convert the representation of a Sudoku solution as returned from
    the method CSP.backtracking_search(), into a human readable
    representation.
    """
    for row in range(9):
        for col in range(9):
            print(solution['%d-%d' % (row, col)][0], end=" "),
            if col == 2 or col == 5:
                print('|', end=" "),
        print("")
        if row == 2 or row == 5:
            print('------+-------+------')