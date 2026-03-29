class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        seen = set()
        
        for i in range(size - 1, -1, -1):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.add(nums[i])
        
        return len(nums)