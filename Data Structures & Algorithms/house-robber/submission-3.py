class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [-1] * size

        for i in range(size - 1, -1, -1):
            n = nums[i] + max((dp[i + 2] if i + 2 < size else 0), (dp[i + 3] if i + 3 < size else 0))
            dp[i] = n
        
        return max(dp[0], dp[1] if size > 1 else 0)

