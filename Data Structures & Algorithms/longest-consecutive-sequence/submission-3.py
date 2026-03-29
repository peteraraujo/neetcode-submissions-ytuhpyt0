class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        cur = nums[0]
        count = 1
        res = 1



        
        for i in range(1, len(nums)):
            n = nums[i]
            
            if n == cur:
                continue
            elif n != cur + 1:
                res = max(res, count)
                count = 0
            
            
            cur = n
            count += 1


            

        
        return max(res, count)