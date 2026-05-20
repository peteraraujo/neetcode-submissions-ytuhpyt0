class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = prev = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            prev = max(prev + n, n)
            res = max(res, prev)

        return res
