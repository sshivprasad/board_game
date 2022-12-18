import unittest

from models import Solution, Cell, Board, Constraint


class TestCell(unittest.TestCase):

    def test_eq_impl(self):
        self.assertEqual(Cell(1, 1, 0), Cell(1, 1))
        self.assertEqual(Cell(1, 2, 3), Cell(1, 2, 3))
        self.assertNotEqual(Cell(2, 3, 10), Cell(3, 2, 10))
        self.assertNotEqual(Cell(2, 3, 10), Cell(3, 3, 10))

    def test_lt_impl(self):
        self.assertTrue(Cell(3, 2, 1) < Cell(4, 2, 3))
        self.assertFalse(Cell(4, 1, 4) < Cell(4, 2, 3))

    def test_gt_impl(self):
        self.assertTrue(Cell(4, 1, 4) > Cell(4, 2, 3))
        self.assertFalse(Cell(3, 2, 1) > Cell(4, 2, 3))


class TestConstraintModel(unittest.TestCase):
    def test_unsupported_operator_throws_exception(self):
        with self.assertRaises(ValueError) as ctx:
            Constraint(Cell(1, 2), '=', Cell(2, 1))
        self.assertEqual(str(ctx.exception), f'Invalid Constraint : =')


class TestSolutionModel(unittest.TestCase):

    def test_solution_insufficient_entries_throws_exception(self):
        n = 2
        entries = [9, 2]
        with self.assertRaises(ValueError) as ctx:
            Solution(n, entries)
        self.assertEqual(str(ctx.exception), f'Insufficient entries for a board of {n}*{n}')

    def test_solution_invalid_range_throws_exception(self):
        n = 2
        entries = [9, 2, 2, 1]
        with self.assertRaises(ValueError) as ctx:
            Solution(n, entries)
        self.assertEquals(str(ctx.exception), f'The numbers in the cells must be between 1 and {n}')

    def test_invalid_cell_pos_throws_exception(self):
        n = 2
        entries = [1, 2, 2, 1]
        solution = Solution(n, entries)
        with self.assertRaises(ValueError) as ctx:
            cell_pos = (3, 1)
            solution[cell_pos]
        self.assertEqual(str(ctx.exception), f'The cell row and col number {cell_pos} is invalid')

    def test_solution_cell_matrix(self):
        n = 2
        entries = [1, 2, 2, 1]
        solution = Solution(n, entries)
        self.assertEqual(solution[1, 1], Cell(1, 1, 1))
        self.assertEqual(solution[1, 2], Cell(1, 2, 2))
        self.assertEqual(solution[2, 1], Cell(2, 1, 2))
        self.assertEqual(solution[2, 2], Cell(2, 2, 1))

    def test_solution_get_row_sum(self):
        n = 2
        expected_row_sum = (n * (n + 1)) / 2

        entries = [1, 2, 1, 2]
        solution = Solution(n, entries)
        self.assertEqual(expected_row_sum, solution.get_row_sum(1))
        self.assertEqual(expected_row_sum, solution.get_row_sum(2))

        entries = [1, 1, 2, 2]
        solution = Solution(n, entries)
        self.assertNotEqual(expected_row_sum, solution.get_row_sum(1))
        self.assertNotEqual(expected_row_sum, solution.get_row_sum(2))

    def test_solution_get_col_sum(self):
        n = 2
        expected_col_sum = (n * (n + 1)) / 2

        entries = [1, 2, 2, 1]
        solution = Solution(n, entries)
        self.assertEqual(expected_col_sum, solution.get_col_sum(1))
        self.assertEqual(expected_col_sum, solution.get_col_sum(2))

        entries = [1, 2, 1, 2]
        solution = Solution(n, entries)
        self.assertNotEqual(expected_col_sum, solution.get_col_sum(1))
        self.assertNotEqual(expected_col_sum, solution.get_col_sum(2))


class TestBoardModel(unittest.TestCase):

    def test_constraints_validation(self):
        n = 2
        board = Board(n, [Constraint(Cell(1, 1), '<', Cell(1, 2)),
                          Constraint(Cell(1, 2), '>', Cell(2, 2)),
                          ])

        entries = [1, 2, 2, 1]
        solution = Solution(n, entries)
        self.assertTrue(board.validate_constraints(solution))

        entries = [1, 1, 2, 2]
        solution = Solution(n, entries)
        self.assertFalse(board.validate_constraints(solution))
