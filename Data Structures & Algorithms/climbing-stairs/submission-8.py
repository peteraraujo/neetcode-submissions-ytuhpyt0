class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def dfs(cur):
            if cur >= n:
                return cur == n
            
            if dp[cur] != -1:
                return dp[cur]
            
            val = dfs(cur + 1) + dfs(cur + 2)
            dp[cur] = val
        

            return val
        
        return dfs(0)

