class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)

        l, r = 0, size - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
            
        return nums[r]
