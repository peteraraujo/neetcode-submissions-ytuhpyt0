class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def dfs(node):
            if node == n:
                return 1
            if node > n:
                return 0
            if (val := dp[node]) != -1:
                return val

            temp = dfs(node + 2) + dfs(node + 1)
            
            dp[node] = temp
            return temp
        
        dfs(0)

        return dp[0]
