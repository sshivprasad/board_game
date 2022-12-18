import unittest
import validator
from models import Solution, Constraint, Cell, Board


class TestValidator(unittest.TestCase):

    def test_axis_sum_validator_row(self):
        n = 2
        solution = Solution(n, [1, 2, 1, 2])
        self.assertTrue(validator._validate_axis_sum(solution, axis=0),
                        f'row sum for each row is {(n * (n + 1)) / 2} as expected')
        solution = Solution(n, [1, 1, 2, 2])
        self.assertFalse(validator._validate_axis_sum(solution, axis=0), f'row sum is not {(n * (n + 1)) / 2}')

    def test_axis_sum_validator_col(self):
        n = 2
        solution = Solution(n, [1, 2, 1, 2])
        self.assertFalse(validator._validate_axis_sum(solution, axis=1), f'col sum is not {(n * (n + 1)) / 2}')
        solution = Solution(n, [1, 1, 2, 2])
        self.assertTrue(validator._validate_axis_sum(solution, axis=1),
                        f'col sum for each col is {(n * (n + 1)) / 2} as expected')

    def test_validator_returns_false_for_not_meeting_constraints(self):
        n = 4
        board = Board(n, [Constraint(Cell(1, 1), '>', Cell(1, 2)),
                          Constraint(Cell(4, 1), '>', Cell(4, 2)),
                          Constraint(Cell(3, 2), '<', Cell(4, 2)),
                          Constraint(Cell(2, 3), '>', Cell(3, 3)),
                          ]
                      )
        solution = Solution(n, [1, 2, 3, 4, 2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3])
        self.assertEqual(validator.is_solution_valid(board, solution),
                         (False, 'The solution does not meet the constraints'))

    def test_validator_returns_false_for_repeating_number_along_row(self):
        n = 2
        board = Board(n, [Constraint(Cell(1, 1), '>', Cell(2, 1))])
        solution = Solution(n, [2, 2, 1, 1])
        self.assertEqual(validator.is_solution_valid(board, solution),
                         (False, 'There are repeating numbers in the rows'))

    def test_validator_returns_false_for_repeating_number_along_col(self):
        n = 2
        board = Board(n, [Constraint(Cell(1, 1), '<', Cell(1, 2))])
        solution = Solution(n, [1, 2, 1, 2])
        self.assertEqual(validator.is_solution_valid(board, solution),
                         (False, 'There are repeating numbers in the columns'))

    def test_validator_returns_true_for_valid_solution(self):
        n = 4
        board = Board(n, [Constraint(Cell(1, 1), '>', Cell(1, 2)),
                          Constraint(Cell(4, 1), '>', Cell(4, 2)),
                          Constraint(Cell(3, 2), '<', Cell(4, 2)),
                          Constraint(Cell(2, 3), '>', Cell(3, 3)),
                          ]
                      )
        solution = Solution(n, [2, 1, 4, 3, 1, 4, 3, 2, 3, 2, 1, 4, 4, 3, 2, 1])
        self.assertEqual(validator.is_solution_valid(board, solution),
                         (True, 'The solution is Valid.'))
