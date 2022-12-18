import operator


class Cell:
    def __init__(self, row, col, val=0):
        self.row = row
        self.col = col
        self.val = val

    def __gt__(self, other) -> bool:
        return self.val > other.val

    def __lt__(self, other) -> bool:
        return self.val < other.val

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col and self.val == other.val


class Constraint:
    _ops_dict = {
        '>': operator.gt,
        '<': operator.lt,
    }

    def __init__(self, left_cell: Cell, op_char, right_cell: Cell):
        self.left_cell = left_cell
        self.right_cell = right_cell
        self.op = self._lookup_operator(op_char)

    def _lookup_operator(self, op_char):
        try:
            return self._ops_dict[op_char]
        except KeyError:
            raise ValueError(f"Invalid Constraint : {op_char}")


class Solution:
    def __init__(self, n: int, entries: list[int]):
        # check if the dimensions of the solution match the board
        if len(entries) != n * n:
            raise ValueError(f'Insufficient entries for a board of {n}*{n}')
        # check if all the numbers in the solution are between 1 and n
        if not all(1 <= num <= n for num in entries):
            raise ValueError(f'The numbers in the cells must be between 1 and {n}')
        self.n = n
        self.entries = entries
        self._cells: list[list[Cell]] = self._prepare_cell_matrix()

    def __getitem__(self, cell_pos: tuple):
        row_num, col_num = cell_pos
        try:
            return self._cells[row_num - 1][col_num - 1]
        except IndexError:
            raise ValueError(f'The cell row and col number {row_num, col_num} is invalid')

    def _prepare_cell_matrix(self) -> list[list[Cell]]:
        cells = []
        entries_iter = iter(self.entries)
        for row_num in range(1, self.n + 1):
            row = []
            for col_num in range(1, self.n + 1):
                row.append(Cell(row_num, col_num, next(entries_iter)))
            cells.append(row)
        return cells

    def get_row_sum(self, row_num):
        row = self._cells[row_num - 1]
        row_sum = 0
        for cell in row:
            row_sum += cell.val
        return row_sum

    def get_col_sum(self, col_num):
        col_sum = 0
        for row_idx in range(self.n):
            col_sum += self._cells[row_idx][col_num - 1].val
        return col_sum


class Board:
    def __init__(self, n: int, constraints: list[Constraint]):
        self.n = n
        self.constraints = constraints

    def validate_constraints(self, solution: Solution) -> bool:
        for constraint in self.constraints:
            left_cell_row = constraint.left_cell.row
            left_cell_col = constraint.left_cell.col
            right_cell_row = constraint.right_cell.row
            right_cell_col = constraint.right_cell.col

            left_cell = solution[left_cell_row, left_cell_col]
            right_cell = solution[right_cell_row, right_cell_col]
            op = constraint.op

            if not op(left_cell, right_cell):
                return False
        return True
