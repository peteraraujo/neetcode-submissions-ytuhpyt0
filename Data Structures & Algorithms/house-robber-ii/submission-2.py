class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 1:
            return nums[-1]
        
        def solve(s, e):
            h1, h2 = nums[e - 1], nums[e]
            for i in range(e - 2, s - 1, -1):
                val = nums[i] + max(h2, h1 - nums[i + 1])
                h1, h2 = val, h1
            return max(h1, h2)
        
        return max(solve(0, size - 2), solve(1, size - 1))
        



