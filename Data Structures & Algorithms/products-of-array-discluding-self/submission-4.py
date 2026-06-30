class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        lr = [1]
        prev = nums[0]

        for i in range(1, size):
            lr.append(prev)
            prev *= nums[i]
        
        
        rl = [1]
        prev = nums[-1]

        for i in range(size - 2, -1, -1):
            rl.append(prev)
            prev *= nums[i]
        
        # rl.reverse()

        for i in range(size):
            lr[i] *= rl[size - (1 + i)] 

        return lr