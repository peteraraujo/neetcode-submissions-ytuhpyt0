class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)

        l, r = 0, size - 1

        if nums[0] <= nums[-1]:
            return nums[0]

        while l < r:
            m = (l + r) // 2

            if nums[l] > nums[m]:
                r = m
            else:
                l = m
            
            if r - l <= 1:
                break
            
        return nums[r]
