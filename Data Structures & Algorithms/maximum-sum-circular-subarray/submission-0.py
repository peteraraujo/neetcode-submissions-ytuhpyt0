class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)

        res = float('-inf')
        
        for i in range(size):
            cur = 0
            for j in range(i, i + size):
                cur += nums[j % size]
                res = max(res, cur)
        
        return res
