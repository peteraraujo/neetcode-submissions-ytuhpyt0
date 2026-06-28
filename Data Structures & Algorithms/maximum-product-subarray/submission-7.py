class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)

        res = float('-inf')
        

        for i in range(size):
            cur = nums[i]
            res = max(res, cur)

            for j in range(i + 1, size):
                cur *= nums[j]
                res = max(res, cur)
            
            
        
        return res
