from models import Board, Constraint, Cell
from validator import is_solution_valid


def main():
    board = Board(n=4,
                  constraints=[Constraint(Cell(1, 1), '>', Cell(1, 2)),
                               Constraint(Cell(4, 1), '>', Cell(4, 2)),
                               Constraint(Cell(3, 2), '<', Cell(4, 2)),
                               Constraint(Cell(2, 3), '>', Cell(3, 3)),
                               ]
                  )

    solution = [[Cell(1, 1, 2), Cell(1, 2, 1), Cell(1, 3, 4), Cell(1, 4, 3)],
                [Cell(2, 1, 1), Cell(2, 2, 4), Cell(2, 3, 3), Cell(2, 4, 2)],
                [Cell(3, 1, 3), Cell(3, 2, 2), Cell(3, 3, 1), Cell(3, 4, 4)],
                [Cell(4, 1, 4), Cell(4, 2, 3), Cell(4, 3, 2), Cell(4, 4, 1)],
                ]

    is_valid, validator_msg = is_solution_valid(board, solution)
    print(f'{is_valid} | {validator_msg}')


if __name__ == '__main__':
    main()
