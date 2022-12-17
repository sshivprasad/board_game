from models import Board, Constraint, Cell, Solution
from validator import is_solution_valid


def main():
    n = 4
    board = Board(n, constraints=[Constraint(Cell(1, 1), '>', Cell(1, 2)),
                                  Constraint(Cell(4, 1), '>', Cell(4, 2)),
                                  Constraint(Cell(3, 2), '<', Cell(4, 2)),
                                  Constraint(Cell(2, 3), '>', Cell(3, 3)),
                                  ]
                  )

    # cell values row-wise
    cell_values = [2, 1, 4, 3, 1, 4, 3, 2, 3, 2, 1, 4, 4, 3, 2, 1]
    valid_solution = Solution(n, cell_values)
    is_valid, validator_msg = is_solution_valid(board, valid_solution)
    print(f'{cell_values} - {is_valid} | {validator_msg}')

    # cell values row-wise
    cell_values = [2, 1, 4, 3, 1, 4, 3, 2, 3, 1, 2, 4, 4, 3, 2, 1]
    invalid_solution = Solution(n, cell_values)
    is_valid, validator_msg = is_solution_valid(board, invalid_solution)
    print(f'{cell_values} - {is_valid} | {validator_msg}')


if __name__ == '__main__':
    main()
