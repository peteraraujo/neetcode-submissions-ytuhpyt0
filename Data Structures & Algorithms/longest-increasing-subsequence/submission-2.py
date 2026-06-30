class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size  = len(nums)

        dp = [1] * size
        res = 0

        for i in range(size):
            n = nums[i]

            prevMax = 0

            for j in range(i - 1, -1, -1):
                prevNum = nums[j]
                if prevNum < n:
                    prevMax = max(prevMax, dp[j])
            
            dp[i] = prevMax + 1
            res = max(res, prevMax + 1)
        
        return res