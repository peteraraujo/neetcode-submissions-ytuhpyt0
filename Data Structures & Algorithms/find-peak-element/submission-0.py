class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)

        for i in range(size):
            l = nums[i - 1] if i - 1 >= 0 else float('-inf')
            r = nums[i + 1] if i + 1 < size else float('-inf')
            n = nums[i]

            if n > l and n > r:
                return i

