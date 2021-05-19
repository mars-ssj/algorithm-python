class Knapsack(object):

    def __init__(self) -> None:
        super().__init__()
        self.max_weight = -1

    def dp(self, cn, cw, w, weights, n):
        '''
            w: 背包容纳重量
            cw: 当前重量
            weights: 物品重量数组
            n: 共多少个物品
            cn: 当前遍历到第几个
        '''
        if cn == n or cw == w:
            if w > self.max_weight:
                self.max_weight = w
            return
        self.dp(cn+1, cw, w, weights, n)
        if cw + weights[cn] <= w:
            self.dp(cn+1, cw+weights[cn], w, weights, n)
