class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        s = f = 0
        res = 0

        for i in range(1, size):
            cur = prices[i]
            prev = prices[i - 1]

            if cur < prev:
                res += prices[f] - prices[s]
                s = f = i
            else:
                f += 1
        
        res += prices[f] - prices[s] 
        return res


        