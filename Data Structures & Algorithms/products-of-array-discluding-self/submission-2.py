class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        pre = [1] * (size + 1)
        suf = [1] * (size + 1)

        for i in range(size):
            pre[i + 1] = pre[i] * nums[i]

        for i in range((size + 1) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]
        
        res = [0] * size

        for i in range(size):
            res[i] = pre[i] * suf[i + 1]
            
        return res
        
        