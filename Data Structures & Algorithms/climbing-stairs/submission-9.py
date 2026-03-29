class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        for cur in range(n, 0, -1):
            if cur == n:
                dp[cur] = 1
                continue
            if cur == n - 1:
                dp[cur] = 2
                continue
            
            val = dp[cur + 1] + dp[cur + 2]

            dp[cur] = val
        

            
        
        return dp[1]

