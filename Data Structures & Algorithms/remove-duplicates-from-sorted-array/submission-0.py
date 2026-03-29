class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size -1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)