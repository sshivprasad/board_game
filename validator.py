from models import Board, Solution


def is_solution_valid(board: Board, solution: Solution) -> (bool, str):
    n = board.n
    # check if solution passes all the constraints of the board
    is_within_constraints = board.validate_constraints(solution)
    if not is_within_constraints:
        return False, 'The solution does not meet the constraints'
    # check if the sum of each row is equal to n(n+1)/2
    is_row_sum_valid = _validate_axis_sum(solution, axis=0)
    if not is_row_sum_valid:
        return False, 'There are repeating numbers in the rows'
    # check if the sum of each col is equal to n(n+1)/2
    is_col_sum_valid = _validate_axis_sum(solution, axis=1)
    if not is_col_sum_valid:
        return False, 'There are repeating numbers in the columns'
    return True, 'The solution is Valid.'


def _validate_axis_sum(solution: Solution, axis: int) -> bool:
    n = solution.n
    expected_sum = (n * (n + 1)) / 2
    for num in range(1, n + 1):
        axis_sum = solution.get_row_sum(num) if axis == 0 else solution.get_col_sum(num)
        if axis_sum != expected_sum:
            return False
    return True
