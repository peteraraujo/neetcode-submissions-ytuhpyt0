class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        if size < 2:
            return min(cost)

        dp = [-1] * size
        dp[-1], dp[-2] = cost[-1], cost[-2]
        
        for i in range(size - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])




        