'''八皇后问题'''
class Queens(object):

    def __init__(self) -> None:
        super().__init__()
        self.results = [0 for _ in range(8)]
        self.count = 0

    def cal_8_queens(self, row):
        if row == 8:
            self.print_queens()
            return
        for column in range(8):
            if self.is_ok(row, column):
                self.results[row] = column
                self.cal_8_queens(row+1)

    def print_queens(self):
        self.count += 1
        for row in range(8):
            for column in range(8):
                if self.results[row] == column:
                    print('Q ', end='')
                else:
                    print('* ', end='')
            print()
        print()

    def is_ok(self, row, column):
        left_up, right_up = column - 1, column + 1
        row_index = row - 1
        while row_index >= 0:
            if self.results[row_index] == column:
                return False
            if left_up >= 0 and self.results[row_index] == left_up:
                return False
            if right_up < 8 and self.results[row_index] == right_up:
                return False
            row_index -= 1
            left_up -= 1
            right_up += 1
        return True




