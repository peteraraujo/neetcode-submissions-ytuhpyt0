class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0

        for n in nums:
            if n - 1 in nums:
                continue
            
            count = 1
            while n + count in nums:
                count += 1
            
            res = max(res, count)

        return res