class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        if size < 2:
            return min(cost)

        prev2, prev1 = cost[-1], cost[-2]
        
        for i in range(size - 3, -1, -1):
            val = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, val
        
        return min(prev1, prev2)


            # 1    2     3
            # i  prev1 prev2




        