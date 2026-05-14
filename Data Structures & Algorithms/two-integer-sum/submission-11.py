class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        rems = {}

        for i in range(size):
            rem = target - nums[i]
            if rem in rems:
                return [rems[rem], i]
            else:
                rems[nums[i]] = i
        
        