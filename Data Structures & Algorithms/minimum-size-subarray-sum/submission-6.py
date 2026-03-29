class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)

        res = float("inf")

        l = 0
        cur = 0

        for r in range(size):

            cur += nums[r]

            while cur >= target:
                res = min(res, r - l + 1)

                cur -= nums[l]
                l += 1
        
        
        return 0 if res == float("inf") else res

            