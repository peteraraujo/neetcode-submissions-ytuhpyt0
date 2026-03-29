class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        
        dp = [-1] * size

        def dfs(i):
            if i >= size:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            

            val = nums[i] +  max(dfs(i + 3), dfs(i + 2))
            dp[i] =  val

            return val
        
    
        return max(dfs(0), dfs(1))