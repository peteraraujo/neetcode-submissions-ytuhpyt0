class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        
        closest = size - 1

        for i in range(size - 2, 0, -1):
            current = nums[i]

            if (reach := i + current) >= closest:
                closest = i
        
        return nums[0] >= closest