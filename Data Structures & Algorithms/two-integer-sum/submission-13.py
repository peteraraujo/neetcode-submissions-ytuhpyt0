class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        
        rems = {} # value : index

        for i in range(size):
            n = nums[i]
            diff = target - n

            if diff in rems:
                return [rems[diff], i]
            
            rems[n] = i
        