class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        count = 0

        cur = -101
        for i in range(size):
            if nums[i] == cur:
                nums[i] = None
            else:
                cur = nums[i]
                count += 1
        

        l = 0
        for r in range(size):
            if nums[r] == None:
                continue
            
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        
        return count
