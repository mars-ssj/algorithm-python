'''实现01背包问题'''
class Knapsack(object):
    
    def __init__(self) -> None:
        super().__init__()
        self.max_weight = -1
    
    def solution(self, weights, weight_limit):
        self.action(0, 0, weight_limit, weights, len(weights))

    def action(self, cn, cw, w, weights, n):
        '''
            w: 背包容纳重量
            cw: 当前重量
            weights: 物品重量数组
            n: 共多少个物品
            cn: 当前遍历到第几个
        '''
        if cn == n or cw == w:
            if cw > self.max_weight:
                self.max_weight = cw
            return
        self.action(cn+1, cw, w, weights, n)
        if cw + weights[cn] <= w:
            self.action(cn+1, cw+weights[cn], w, weights, n)

class KnapsackMaxValue(object):

    def __init__(self) -> None:
        super().__init__()
        self.max_value = -1
    
    def solution(self, weights, weight_limit, values):
        self.action(0, 0, weight_limit, weights, 0, values, len(weights))

    def action(self, cn, cw, w, weights, cv, values, n):
        if cw == w or cn == n:
            if cv > self.max_value:
                self.max_value = cv
            return
        self.action(cn+1, cw, w, weights, cv, values, n)
        if cw + weights[cn] <= w:
            self.action(cn+1, cw+weights[cn], w, weights, cv+values[cn], values, n)
