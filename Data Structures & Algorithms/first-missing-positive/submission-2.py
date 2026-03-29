class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        size = len(nums)

        for i in range(size):
            if nums[i] < 0:
                nums[i] = 0
            
        
        
        for i in range(size):
            n = abs(nums[i])
            ic = n - 1

            if 0 <= ic < size:
                
                if nums[ic] == 0:
                     nums[ic] = -n
                     
                else:
                    nums[ic] = -abs(nums[ic])

        print(nums)
        
        
        for n in range(1, size + 1):
            if nums[n - 1] >= 0:
                return n
        
        
        return n + 1
        

        