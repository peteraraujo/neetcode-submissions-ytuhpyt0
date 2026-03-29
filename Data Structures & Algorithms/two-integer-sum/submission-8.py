class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        saved = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in saved:
                return [saved[diff], i]
            
            saved[n] = i
            
        















