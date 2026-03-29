class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        
        h1, h2 = nums[-2], nums[-1]

        for i in range(size - 3, -1, -1):
            n = nums[i] + max(h2, h1 - nums[i + 1])
            h1, h2 = n, h1
        
        return max(h1, h2)