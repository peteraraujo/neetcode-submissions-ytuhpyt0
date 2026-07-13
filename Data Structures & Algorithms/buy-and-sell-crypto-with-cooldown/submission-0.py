class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        size = len(prices)
        dp = {}

        def dfs(i, buying):
            if i >= size:
                return 0

            key = (i, buying)
            
            if key in dp:
                return dp[key]
            
            cd = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                dp[key] = max(buy, cd)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[key] = max(sell, cd)
            
            return dp[key]

        return dfs(0, True)