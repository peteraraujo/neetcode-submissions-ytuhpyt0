class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 1
        
        res = 1
        l = 1

        for r in range(1, size):
            if nums[r] == nums[r - 1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                res += 1
        
        return res