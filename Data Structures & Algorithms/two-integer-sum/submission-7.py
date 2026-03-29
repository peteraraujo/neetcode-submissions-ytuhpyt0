class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        rems = dict()

        for i, n in enumerate(nums):
            rem = target - n

            if rem in rems:
                return [rems[rem], i]
            
            rems[n] = i















