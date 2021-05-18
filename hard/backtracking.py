results = [0 for _ in range(8)]

def print_queens():
    for row in range(8):
        for column in range(8):
            if results[row] == column:
                print('Q ', end='')
            else:
                print('* ', end='')
        print()
    print()

def is_ok(row: int, column: int)-> bool:
    left_up, right_up = column - 1, column + 1
    row_index = row - 1
    while row_index >= 0:
        if results[row_index] == column:
            return False
        if left_up >= 0 and results[row_index] == left_up:
            return False
        if right_up < 8 and results[row_index] == right_up:
            return False
        row_index -= 1
        left_up -= 1
        right_up += 1
    return True

def cal_8_queens(row: int):
    if row == 8:
        print_queens()
        return
    for column in range(8):
        if is_ok(row, column):
            results[row] = column
            cal_8_queens(row+1)

if __name__ == "__main__":
    cal_8_queens(0)