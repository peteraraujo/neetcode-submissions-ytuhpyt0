class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {} # rem, index

        for i in range(len(nums)):

            n = nums[i]
            rest = target - n

            if rest in rem:
                return [rem[rest], i]
            
            
            rem[n] = i