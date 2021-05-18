results = [0 for _ in range(8)]
count = 0

def print_queens():
    global count
    count += 1
    for row in range(8):
        for column in range(8):
            if results[row] == column:
                print('Q ', end='')
            else:
                print('* ', end='')
        print()
    print()

def is_ok(row, column):
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

def cal_8_queens(row):
    if row == 8:
        print_queens()
        return
    for column in range(8):
        if is_ok(row, column):
            results[row] = column
            cal_8_queens(row+1)

# w: 背包容纳重量
# cw: 当前重量
# weights: 物品重量数组
# n: 共多少个物品
# cn: 当前遍历到第几个
max_weight = -1
def dp(cn, cw, w, weights, n):
    if cn == n or cw == w:
        global max_weight
        if w > max_weight:
            max_weight = w
        return
    dp(cn+1, cw, w, weights, n)
    if cw + weights[cn] <= w:
        dp(cn+1, cw+weights[cn], w, weights, n)


if __name__ == "__main__":
    # cal_8_queens(0)
    weights = [2, 2, 4, 6, 3]
    dp(0, 0, 9, weights, 5)
    print(max_weight)