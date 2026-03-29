class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()

        cur = nums[0]
        count = 1
        res = 1

        print(nums)
        for n in nums[1:]:
            if n != cur + 1:
                res = max(res, count)
                count = 0
            
            cur = n
            count += 1
        
        return max(res, count)
