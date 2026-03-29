class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        l1 = [1] * len(nums)

        s = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            l1[i] = s

            s *= num
        
        s = nums[-1]

        for i in range(len(nums) - 1, 0, -1):
            
            l1[i - 1] = s * l1[i - 1]
            s *= nums[i - 1]

        return l1

            

            
            





