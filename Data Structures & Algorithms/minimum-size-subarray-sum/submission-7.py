class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        
        minw = size + 1
        w = 0
        l = 0

        for r in range(size):
            w += nums[r]
            
            while w >= target:
                minw = min(minw, r - l + 1)
                w -= nums[l]
                l += 1
        
        return 0 if minw == size + 1 else minw