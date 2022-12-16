import unittest
import validator
from models import Cell


class TestValidator(unittest.TestCase):

    def test_row_sum_validator_valid_input(self):
        n = 2
        solution = [[Cell(1, 1, 1), Cell(1, 2, 2)],
                    [Cell(2, 1, 1), Cell(2, 2, 2)],
                    ]
        self.assertTrue(validator._validate_row_sum(n, solution),
                        f'row sum for each row is {(n * (n + 1)) / 2} as expected')

    def test_row_sum_validator_invalid_input(self):
        n = 2
        solution = [[Cell(1, 1), Cell(1, 2, 3)],
                    [Cell(2, 1, 2), Cell(2, 2, 3)],
                    ]
        self.assertFalse(validator._validate_row_sum(n, solution), f'row sum is not {(n * (n + 1)) / 2}')

    def test_col_sum_validator_valid_input(self):
        n = 2
        solution = [[Cell(1, 1, 1), Cell(1, 2, 3)],
                    [Cell(2, 1, 2), Cell(2, 2)],
                    ]
        self.assertTrue(validator._validate_col_sum(n, solution),
                        f'col sum for each col is {(n * (n + 1)) / 2} as expected')

    def test_col_sum_validator_invalid_input(self):
        n = 2
        solution = [[Cell(1, 1, 1), Cell(1, 2, 2)],
                    [Cell(2, 1, 1), Cell(2, 2, 2)],
                    ]
        self.assertFalse(validator._validate_col_sum(n, solution), f'col sum is not {(n * (n + 1)) / 2}')

    def test_solution_validator_incorrect_dimension(self):
        # TODO what if user enters two values for the same row and col idx
        pass
