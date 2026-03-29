class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            n = nums[i]
            rem = target - n
            if rem in prev:
                return [prev[rem], i]
            prev[n] = i
        