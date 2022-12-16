from models import Board, Cell


def is_solution_valid(board: Board, solution: list[list[Cell]]) -> (bool, str):
    n = board.n
    # check if the dimensions of the solution match the board
    if not all(len(row) == n for row in solution) or len(solution) != n:
        return False, f'Solution matrix should be of the dimension {n}*{n}'
    # check if all the numbers in the board are between 1 and n
    is_within_range = all(0 <= cell.val <= n for row in solution for cell in row)
    if not is_within_range:
        return False, f'The numbers in the cells must be between 1 and {n}'
    # check if solution passes all the constraints of the board
    is_within_constraints = board.validate_constraints(solution)
    if not is_within_constraints:
        return False, f'The solution does not meet the constraints'
    # check if the sum of each row is equal to n(n+1)/2
    is_row_sum_valid = _validate_row_sum(n, solution)
    if not is_row_sum_valid:
        return False, f'There is a repeating number in one of the rows'
    # check if the sum of each col is equal to n(n+1)/2
    is_col_sum_valid = _validate_col_sum(n, solution)
    if not is_col_sum_valid:
        return False, f'There is a repeating number in one of the columns'
    return True, 'The solution is Valid.'


def _validate_row_sum(n, solution: list[list[Cell]]) -> bool:
    expected_row_sum = (n * (n + 1)) / 2
    for row in solution:
        row_sum = 0
        for cell in row:
            row_sum += cell.val
        if row_sum != expected_row_sum:
            return False
    return True


def _validate_col_sum(n, solution: list[list[Cell]]) -> bool:
    expected_col_sum = (n * (n + 1)) / 2
    for col_idx in range(n):
        col_sum = 0
        for row_idx in range(n):
            col_sum += solution[row_idx][col_idx].val
        if col_sum != expected_col_sum:
            return False
    return True
