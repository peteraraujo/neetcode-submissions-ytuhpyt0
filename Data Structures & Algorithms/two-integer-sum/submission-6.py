class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        rems = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in rems.keys():
                return [rems[diff], i]

            if n not in rems.keys():
                rems[n] = i

        return []
















