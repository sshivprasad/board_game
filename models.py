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


class Constraint:
    _ops_dict = {
        '>': operator.gt,
        '<': operator.lt,
    }

    def __init__(self, left_cell_idx: Cell, op_char, right_cell_idx: Cell):
        self.left_cell_idx = left_cell_idx
        self.right_cell_idx = right_cell_idx
        self.op = self._lookup_operator(op_char)

    def _lookup_operator(self, op_char):
        try:
            return self._ops_dict[op_char]
        except KeyError:
            raise ValueError(f"Invalid Constraint : {op_char}")


class Board:
    def __init__(self, n, constraints: list[Constraint]):
        self.n = n
        self.constraints = constraints

    def validate_constraints(self, solution: list[list[Cell]]) -> bool:
        for constraint in self.constraints:
            left_cell_row = constraint.left_cell_idx.row - 1
            left_cell_col = constraint.left_cell_idx.col - 1
            right_cell_row = constraint.right_cell_idx.row - 1
            right_cell_col = constraint.right_cell_idx.col - 1

            left_cell = solution[left_cell_row][left_cell_col]
            right_cell = solution[right_cell_row][right_cell_col]
            op = constraint.op

            if not op(left_cell, right_cell):
                return False
        return True
