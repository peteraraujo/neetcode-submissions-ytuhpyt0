class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i1 in range(size - 1):
            for i2 in range(i1 + 1, size):
                if nums[i1] + nums[i2] == target:
                    return [i1, i2]