class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        history = [0] * size

        for n in nums:
            if history[n - 1]:
                return n
            history[n - 1] = 1
        