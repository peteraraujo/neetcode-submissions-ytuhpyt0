class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        r = w = b = 0
        for c in nums:
            if c == 0:
                r += 1
            elif c == 1:
                w += 1
            else:
                b += 1
        
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b