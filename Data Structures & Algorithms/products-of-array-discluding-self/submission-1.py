class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        s = nums[0]
        for i in range(1, len(nums)):
            res[i] *= s
            s *= nums[i]
        
        s = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= s
            s *= nums[i]
        

        return res



























