'''01背包问题'''
class Knapsack(object):

    def __init__(self) -> None:
        super().__init__()
    
    def solution_max_weight(self, weights, weight_limit, n):
        states = [[False for _ in range(weight_limit+1)] for _ in range(n)]

        states[0][0] = True
        if weights[0] <= weight_limit:
            states[0][weights[0]] = True
        
        for i in range(1, n):
            for j in range(0, weight_limit+1):
                if states[i-1][j]:
                    states[i][j] = True
                    if j + weights[i] <= weight_limit:
                        states[i][j+weights[i]] = True
        
        for k in range(weight_limit, -1, -1):
            if states[n-1][k]:
                return k
        return 0


    def solution_max_weight2(self, weights, weight_limit, n):
        states = [False for _ in range(weight_limit+1)]

        states[0] = True
        if weights[0] <= weight_limit:
            states[weights[0]] = True
        
        for i in range(1, n):
            # j的约束：j + weights[i] <= weight_limit，因此j <= weight_limit -  weights[i]
            # 从大到小遍历，否则可能会有新的状态增加，导致计算不准确
            for j in range(weight_limit-weights[i], -1, -1):
                if states[j]:
                    states[j+weights[i]] = True

        for k in range(weight_limit, -1, -1):
            if states[k]:
                return k
        return 0

    def solution_max_value(self, weights, weight_limit, n, values):
        states = [[-1 for _ in range(weight_limit+1)] for _ in range(n)]

        states[0][0] = 0
        if weights[0] <= weight_limit:
            states[0][weights[0]] = values[0]
        
        for i in range(1, n):
            for j in range(0, weight_limit+1):
                if states[i-1][j] >= 0:
                    states[i][j] = states[i-1][j]
                    if j + weights[i] <= weight_limit:
                        cv = states[i-1][j] + values[i]
                        print(cv)
                        if cv > states[i][j+weights[i]]:
                            states[i][j+weights[i]] = cv
            
            # for j in range(0, weight_limit-weights[i]+1):
            #     if states[i-1][j] >= 0:
            #         cv = states[i-1][j] + values[i]
            #         if cv > states[i][j+weights[i]]:
            #             states[i][j+weights[i]] = cv
        max_value = -1
        for k in range(weight_limit+1):
            if states[n-1][k] > max_value:
                max_value = states[n-1][k]
        return max_value

    
    def solution_max_value2(self, weights, weight_limit, n, values):
        states = [-1 for _ in range(weight_limit+1)]

        states[0] = 0
        if weights[0] <= weight_limit:
            states[weights[0]] = values[0]
        
        for i in range(1, n):
            for j in range(weight_limit-weights[i], -1, -1):
                if states[j] >= 0:
                    cv = states[j] + values[i]
                    if cv > states[j+weights[i]]:
                        states[j+weights[i]] = cv
        max_value = -1
        for k in range(weight_limit+1):
            if states[k] > max_value:
                max_value = states[k]
        return max_value
    