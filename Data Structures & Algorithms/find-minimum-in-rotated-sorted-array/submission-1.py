class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        size = len(nums)
        l, r = 0, size - 1

        while l < r:
            m = (l + r) // 2
            
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        print(l)
        return nums[l + 1]
            